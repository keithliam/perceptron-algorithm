def getDataVariablesAsString():
	string = ''
	for ctr in range(0, xLength - 1):
		string += 'x' + str(ctr) + '\t\t'
	string += 'b\t\t'
	for ctr in range(0, xLength - 1):
		string += 'w' + str(ctr) + '\t\t'
	string += 'wb\t\ta\t\ty\tz'
	return string

def getDataAsString():
	string = ''	
	for ctr in range(0, dLength):
		for ctr1 in range(0, xLength - 1):
			string += ('%6.4f' % data['x'][ctr1][ctr]) + '\t'
		string += ('%6.4f' % b) + '\t'
		for ctr1 in range(0, xLength):
			string += ('%6.4f' % data['w'][ctr1][ctr]) + '\t'
		string += ('%6.4f' % data['a'][ctr]) + '\t' + str(data['y'][ctr]) + '\t' + str(data['z'][ctr]) + '\n'
	return string

data = {}
data['x'] = []; data['w'] = []; data['a'] = []; data['y'] = []; data['z'] = []

# read first 3 lines
inputFile = open('input.txt', 'r')
r = float(inputFile.readline())
t = float(inputFile.readline())
b = float(inputFile.readline())

# read rest of the data
xLength = 0; dLength = 0
first = True
line = inputFile.readline()
dLength = 0
while line != '':
	dLength += 1
	line = line.split(' ')
	if first: 
		xLength = len(line)
		for ctr in range(0, xLength - 1):
			data['x'].append([])
			data['w'].append([])
		data['w'].append([])
	for ctr in range(0, xLength - 1):
		data['x'][ctr].append(float(line[ctr]))
	
	if line[xLength - 1][-1:] == '\n':
		data['z'].append(int(line[xLength - 1][:-1]))
	else:
		data['z'].append(int(line[xLength - 1]))

	line = inputFile.readline()
	first = False
inputFile.close()

# initiate perceptron algorithm
first = True
limit = 15000
for ctr in range(0, xLength - 1):
	data['w'][ctr].append(0)
data['w'][xLength - 1].append(0)
for x in range(0, limit):
	for ctr in range(0, dLength):
		wTemp = []

		a = 0
		for ctr1 in range(0, xLength - 1):
			a += data['x'][ctr1][ctr] * data['w'][ctr1][ctr]
		a += b * data['w'][xLength - 1][ctr]
		data['a'].append(a)
		
		if a > t:
			data['y'].append(1)
		else:
			data['y'].append(0)

		error = data['z'][ctr] - data['y'][ctr]

		if ctr != dLength - 1:
			for ctr1 in range(0, xLength - 1):
				data['w'][ctr1].append(data['w'][ctr1][ctr] + (r * data['x'][ctr1][ctr] * error))
			data['w'][xLength - 1].append(data['w'][xLength - 1][ctr] + (r * b * error))
		else:
			for ctr1 in range(0, xLength - 1):
				wTemp.append(data['w'][ctr1][ctr] + (r * data['x'][ctr1][ctr] * error))
			wTemp.append(data['w'][xLength - 1][ctr] + (r * b * error))

	converge = True
	for ctr in range(0 , xLength):
		value = data['w'][ctr][0]
		for ctr1 in range(1, dLength):
			if data['w'][ctr][ctr1] != value:
				converge = False
	if converge:
		break
	elif x == limit - 1:
		break

	# reset all values
	data['a'] = []
	data['y'] = []
	for ctr in range(0, xLength):
		data['w'][ctr] = []

	for ctr in range(0, xLength):
		data['w'][ctr].append(wTemp[ctr])

# write output to file
outputFile = open('output.txt', 'w')
outputFile.write(getDataVariablesAsString() + '\n' + getDataAsString())
outputFile.close()