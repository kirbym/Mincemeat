import mincemeat
import sys

#Opens given textfile read as command line argument, $python mathstats.py small.txt
numfile = open(sys.argv[1], 'r')

#Read each line of text, strip whitespace characters, convert to integers
data = numfile.readlines()
data = [line.strip() for line in data]
data = [int(line) for line in data]

numfile.close()

#split data into chunks
data1 = data[0:len(data)/4]
data2 = data[len(data)/4:len(data)/2]
data3 = data[len(data)/2:3*len(data)/4]
data4 = data[3*len(data)/4:len(data)]

datasource = {0: data1, 1: data2, 2: data3, 3: data4}

def mapfn(key, value):
    yield 'Count', len(value)
    yield 'Sum', sum(value)
    yield 'xSqr', sum(map(lambda a: a**2, value))

def reducefn(key, vlist):
	return sum(vlist)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
#print results

expValueXsqr = results['xSqr']/float(results['Count'])
expValueX2 = (results['Sum']/float(results['Count']))**2
StdDev = (expValueXsqr - expValueX2)**(.5)

print "Count: ", results['Count']
print "Sum: ", results['Sum']
print "StdDev: ", StdDev
