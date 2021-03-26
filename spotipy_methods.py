def read_spot_data(name):
	dataFile = './Spotipy_data/clients/{0}.txt'.format(name)
	file = open(dataFile)
	data = ''
	for lines in file:
		data += lines
	file.close()
	return parse_spot_data(data);
def parse_spot_data(data):
	retList = []
	for prop in data.split('\n'):
		tempList = prop.split(' = ')
		retList.append((tempList[0],tempList[1]))
	return retList