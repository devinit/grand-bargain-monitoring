import collections
import csv
import os

# local configuration
data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')
data_path_remote = os.path.join(data_path, 'remote')
data_path_static = os.path.join(data_path, 'static')


def load_csv_file(loc_type, name):
	"""
	Loads CSV data into a list of dictionaries.

	Params:
		loc_type (str): Either 'remote' or 'static'. Static is assumed if an incorrect value is provided.
		name (str): The combined name and filetype of the file to load.

	Returns:
		list of dict: The data read from the file.
		Keys in each element are the values specified in the heading row of the CSV file.

	Note:
		The CSV file must contain a header row.

	Warning:
		Behavior when loading data from a location that does not contain valid CSV data is unspecified.
	"""
	path = data_path_remote if (loc_type == 'remote') else data_path_static

	# TODO: Properly deal with files that don't exist
	with open(os.path.join(path, name), 'r', encoding='utf-8') as f:
		reader = csv.DictReader(f)

		return list(reader)


def publisherify_data(base_info, summary_stats):
	"""
	Converts data to be in a format that allows direct querying by publisher.

	Params:
		base_info (list of dict): A list of dictionaries containing the base info.
		summary_stats (list of dict): A list of dictionaries containing the summary stats.

	Returns:
		dict of dict: The keys in the first-level dictionary are publisher registry IDs.
			Keys at the second level are names of statistics parsed from data file headers.
	"""
	data = collections.defaultdict(dict)
	all_values = ['baseline', 'first_published', 'name_en', 'Timeliness', 'Forward looking', 'Comprehensive', 'Coverage', 'humanitarian', 'humanitarian_spend_reference', 'humanitarian_spend_iati', 'spend_ratio']

	for row in base_info:
		registry_id = row['registry_id']
		stats = ['baseline', 'first_published', 'name_en']
		for stat in stats:
			data[registry_id][stat] = row[stat]

	for row in summary_stats:
		registry_id = row['Publisher Registry Id']

		# only track data for Grand Bargain signatories
		if registry_id in data:
			stats = ['Timeliness', 'Forward looking', 'Comprehensive', 'Coverage']
			for stat in stats:
				data[registry_id][stat] = row[stat]

	# generate fake data for values we do not yet have
	import random
	import math
	for k in data.keys():
		# until real humanitarian data is available, use a RNG
		# TODO: Use real humanitarian numbers
		data[k]['humanitarian'] = str(random.randint(0, 100))

	# deal with coverage values
	for k in data.keys():
		# until real baseline data is available, use a RNG
		# TODO: Use real baseline numbers
		data[k]['baseline'] = str(random.randint(0, 100))

    # set various coverage values to zero
		data[k]['humanitarian_spend_reference'] = 0
		data[k]['humanitarian_spend_iati'] = 0
		data[k]['spend_ratio'] = 0

	# calculate totals
	for k in data.keys():
		# coverage totals
		if data[k]['spend_ratio'] == 0:
			data[k]['humanitarian_coverage_total'] = 0
		elif data[k]['spend_ratio'] < 40:
			data[k]['humanitarian_coverage_total'] = 40
		elif data[k]['spend_ratio'] < 60:
			data[k]['humanitarian_coverage_total'] = 60
		elif data[k]['spend_ratio'] < 80:
			data[k]['humanitarian_coverage_total'] = 80
		else:
			data[k]['humanitarian_coverage_total'] = 100

	# fill in blanks
	for k in data.keys():
		for k2 in all_values:
			if k2 not in data[k].keys() or data[k][k2] == '':
				data[k][k2] = 0

	# calculate summary
	for k in data.keys():
		high_total= int(data[k]['Timeliness']) + int(data[k]['Forward looking']) + int(data[k]['Comprehensive']) + int(data[k]['humanitarian_coverage_total'])
		data[k]['summary_total'] = round(high_total / 4)

		# progress
		data[k]['progress'] = data[k]['summary_total'] - int(data[k]['baseline'])

	return data


def load_and_format_data():
	"""
	Loads and formats all data to be queried by publisher.

	Returns:
		dict of dict: The keys in the first-level dictionary are publisher registry IDs.
			Keys at the second level are names of statistics parsed from data file headers.
	"""
	base_info = load_csv_file('static', 'base_info.csv')
	summary_stats = load_csv_file('remote', 'summary_stats.csv')
	data_by_publisher = publisherify_data(base_info, summary_stats)

	return data_by_publisher
