#!/usr/bin/env bash

echo "Updating the Data Snapshot"
cd /home/stats/gbm-IATI-Stats/data
# update git and output logs to file

echo "Running IATI Stats"
cd /home/stats/gbm-IATI-Stats
source pyenv/bin/activate
# run relevant script and output logs to file
deactivate

echo "Running IATI Dashboard"
cd /home/dash/gbm-IATI-Dashboard
source pyenv/bin/activate
# run relevant script and output logs to file
deactivate
