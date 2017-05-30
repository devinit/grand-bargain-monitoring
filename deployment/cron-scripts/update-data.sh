#!/usr/bin/env bash

echo "Copying data to Scorecard"

# ensure we're not copying an empty file
num_lines=`cat /home/numbergen/gbm-IATI-Dashboard/web/summary_stats.csv | wc -l`
if [ $num_lines -lt 2 ]
then
    echo "Not enough data to copy"
    exit 1
fi

# copy relevant generated CSVs to scorecard repo
cp /home/numbergen/gbm-IATI-Dashboard/web/summary_stats.csv /var/www/grand-bargain-monitoring/data/remote/summary_stats.csv

echo "Updated Scorecard data"
