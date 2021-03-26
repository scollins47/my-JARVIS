import json

#pre: list of touples [(prop, val), (prop, val),...]
#     the name of the file to write
#     a possible user to tie the data to IN CONSTRUCTION
#post: creates a json file with the input
def write_to_json(input_list, file_name, user = 'unknown'):
	temp = '{}'
	data = json.loads(temp)
	for touple in input_list:
		props = {touple[0]:touple[1]}
		data.update(props);
	with open(file_name, 'w') as outfile:
		json.dump(data, outfile, indent=4)
	print('wrote file ' + file_name)

# pre: the file name to read from, and a possible property inside that file
# post: returns the json file data, or a specific property 
def read_from_json(file_name, prop = 'none'):
	ret = []
	with open(file_name) as json_file:
		data = json.load(json_file)
		try:
			ret = data[prop]
			return ret
		except KeyError:
			print('No ' + prop + ' Property found on the file ')
			return data