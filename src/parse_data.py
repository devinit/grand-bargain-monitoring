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


print(load_data_file('static', 'base_info.csv'))

print(load_csv_file('static', 'base_info.csv'))
