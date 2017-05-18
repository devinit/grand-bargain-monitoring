#!/usr/bin/env bash

echo "Updating the Data Snapshot"
cd /home/stats/gbm-IATI-Stats/data
git checkout automatic > /home/stats/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1
git reset --hard > /home/stats/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1
git clean -df > /home/stats/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1
git pull --ff-only > /home/stats/logs/$(date +\%Y\%m\%d)-snapshot.log 2>&1

echo "Running IATI Stats"
cd /home/stats/gbm-IATI-Stats
source pyenv/bin/activate
# run script to generate stats
./git_dashboard.sh > /home/stats/logs/$(date +\%Y\%m\%d)-stats.log 2>&1
deactivate

echo "Running IATI Dashboard"
cd /home/dash/gbm-IATI-Dashboard
source pyenv/bin/activate
# run script to generate CSVs and such
./git.sh > /home/dashboard/logs/$(date +\%Y\%m\%d)-dashboard.log 2>&1
deactivate

echo "Copying data to Scorecard"
# copy relevant generated CSVs to scorecard repo

echo "Completed data update"
