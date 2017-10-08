data1 = ['fuck', 'shit', 'cunt', 69]
data2 = ['niggers']
data3 = ['aids', 'fuck', 'fuck', 'fuck', 'fuck']


def table(*args):
	line = 0
	longestStr = 0
	longestData = 0
	for data in args:
		if len(data) > longestData:
			longestData = len(data)
		for i in data:
			line = line + len(str(i))
			if len(str(i)) >= longestStr:
				longestStr = len(str(i))
#print('|' + str(i) + ' ' * (longestStr - len(str(i))), end = '')

	dataSetCount = 0
	for dataSet in args:
		dataSetCount = dataSetCount + 1
		itemCount = 0
		print('\n' + '-'*line)
		print('|', end='')
		for item in dataSet:
			itemCount = itemCount + 1
			if itemCount <= len(dataSet):
				print(str(item) + ' ' * (longestStr - len(str(item))), end = '|')

		x = len(dataSet)
		while x < longestData:
			print(' ' * longestStr, end = '|')
			x = x + 1
	print('\n' + '-'*line)


table(data1, data2, data3)
