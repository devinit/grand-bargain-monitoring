#!/usr/bin/env bash

echo "Updating the Data Snapshot"
cd /home/numbergen/gbm-IATI-Stats/data
git checkout automatic > /home/numbergen/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1
git reset --hard > /home/numbergen/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1
git clean -df > /home/numbergen/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1
git pull --ff-only > /home/numbergen/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1

echo "Running IATI Stats"
cd /home/numbergen/gbm-IATI-Stats
source pyenv/bin/activate
# run script to generate stats
./git_dashboard.sh > /home/numbergen/logs/$(date +\%Y\%m\%d)-stats.log 2>&1
deactivate

echo "Running IATI Dashboard"
cd /home/numbergen/gbm-IATI-Dashboard
source pyenv/bin/activate
# run script to generate CSVs and such
./git.sh > /home/numbergen/logs/$(date +\%Y\%m\%d)-dashboard.log 2>&1
deactivate

echo "Completed data update"
