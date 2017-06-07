#!/usr/bin/env bash

echo "Copying summary_stats data to Scorecard"

# ensure we're not copying an empty file
num_lines=`cat /home/numbergen/gbm-IATI-Dashboard/web/summary_stats.csv | wc -l`
if [ $num_lines -lt 400 ]
then
    echo "Not enough summary_stats data to copy"
    exit 1
fi

# copy relevant generated CSVs to scorecard repo
cp /home/numbergen/gbm-IATI-Dashboard/web/summary_stats.csv /var/www/grand-bargain-monitoring/data/app/summary_stats.csv

echo "Copied summary_stats Scorecard data"

echo "Copying humanitarian data to Scorecard"

# ensure we're not copying an empty file
num_lines=`cat /home/numbergen/gbm-IATI-Dashboard/web/humanitarian.csv | wc -l`
if [ $num_lines -lt 400 ]
then
    echo "Not enough humanitarian data to copy"
    exit 1
fi

# copy relevant generated CSVs to scorecard repo
# NOTE: Under 'remote' rather than 'app' as a quick fix switch from downloading from dashboard.iatistandard.org
cp /home/numbergen/gbm-IATI-Dashboard/web/humanitarian.csv /var/www/grand-bargain-monitoring/data/remote/humanitarian.csv

echo "Copied humanitarian Scorecard data"

echo "Removing execution of data"

chmod -x /var/www/grand-bargain-monitoring/data/remote/humanitarian.csv
chmod -x /var/www/grand-bargain-monitoring/data/app/summary_stats.csv

echo "Removed execution of humanitarian data"
