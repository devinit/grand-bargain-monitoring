#!/usr/bin/env python
import os

import requests


# local configuration
remote_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data', 'remote')


# URLs at which data can be found
csv_url_summary_stats = 'http://dashboard.iatistandard.org/summary_stats.csv'


with open(os.path.join(remote_data_path, 'summary_stats.csv'), 'w') as f:
	# load the data to write to the file
	# TODO: Add error handling - URL loading
	response = requests.get(csv_url_summary_stats)

	if not response.ok:
		print('There was a problem loading the Summary Statistics data')

	# TODO: Add error handling - file writing
	f.write(response.text)


# TODO: Add mention of __main__ and main()
