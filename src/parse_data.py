import collections
import csv
import os

# local configuration
data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')
data_path_remote = os.path.join(data_path, 'remote')
data_path_static = os.path.join(data_path, 'static')

# TODO: Make the functions that load something from a file more DRY

def load_csv_file(loc_type, name):
	"""
	Loads CSV data into an array of dictionaries.

	Params:
		loc_type (str): Either 'remote' or 'static'. Static is assumed if an incorrect value is provided.
		name (str): The combined name and filetype of the file to load.

	Returns:
		An array of dictionaries containing the data read from the file.

	Note:
		The CSV file must contain a header row.

	Warning:
		Behavior when loading data from a location that does not contain valid CSV data is unspecified.
	"""
	path = data_path_remote if (loc_type == 'remote') else data_path_static

	# TODO: Properly deal with files that don't exist
	with open(os.path.join(path, name), 'r') as f:
		reader = csv.DictReader(f)

		return list(reader)


def load_data_file(loc_type, name):
	"""
	Loads a data file into a string.

	Params:
		loc_type (str): Either 'remote' or 'static'. Static is assumed if an incorrect value is provided.
		name (str): The combined name and filetype of the file to load.

	Returns:
		A string containing the contents of the file.

	Warning:
		Behavior when a file cannot be correctly read is unspecified.
	"""
	path = data_path_remote if (loc_type == 'remote') else data_path_static

	# TODO: Properly deal with files that don't exist
	with open(os.path.join(path, name), 'r') as f:
		data_str = f.read()

	return data_str


def publisherify_data(base_info, summary_stats):
	"""
	Converts data to be in a format that allows direct querying by publisher.

	Params:
		base_info (array of dict): An array of dictionaries containing the base info.
		summary_stats (array of dict): An array of dictionaries containing the summary stats.

	Returns:
		A dictionary of dictionaries. The keys in the first-level dictionary are publisher registry IDs. Keys at the second level are names of statistics parsed from data file headers.
	"""
	data = collections.defaultdict(dict)

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

	# until real humanitarian data is available, use a RNG
	# TODO: Use real humanitarian numbers
	import random
	for k in data.keys():
		data[k]['humanitarian'] = str(random.randint(0, 100))

	return data


def load_and_format_data():
	"""
	Loads and formats all data to be queried by publisher.

	Returns:
		A dictionary of dictionaries. The keys in the first-level dictionary are publisher registry IDs. Keys at the second level are names of statistics parsed from data file headers.
	"""
	base_info = load_csv_file('static', 'base_info.csv')
	summary_stats = load_csv_file('remote', 'summary_stats.csv')
	data_by_publisher = publisherify_data(base_info, summary_stats)

	return data_by_publisher
