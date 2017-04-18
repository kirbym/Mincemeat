import mincemeat
import sys
import hashlib
from string import ascii_lowercase

hashvalue = sys.argv[1] #get hash value to crack from command line

print "Attacking ", hashvalue

#generate list of lowercase letters and numerals
letters = [ascii_lowercase[l] for l in range(len(ascii_lowercase))]
numerals = [str(n) for n in range(10)]
chars = letters + numerals  #all 36 options for characters
data = []   #all possible 4 or less character passwords of lowercase letters and numerals
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                data.append(c1+c2+c3+c4)
            data.append(c1+c2+c3)
        data.append(c1+c2)
    data.append(c1)

#'chunks' is list of (lists of 100 passwords)
chunks = [data[i:i+250] for i in xrange(0, len(data), 250)]

count = 0
datasource = {}
for chunk in chunks:
    blobdata = {}
    blobdata[hashvalue] = chunk
    datasource[count] = blobdata
    count += 1

#datasource = dict(enumerate(chunks))
#datasource = {}
#datasource[hashvalue] = data

def mapfn(key, value):
    for key in value:
        for v in value[key]:
            if hashlib.md5(v).hexdigest()[:5] == key:
                yield 'Found', v

def reducefn(key, vlist):
    return vlist

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
