#!/usr/bin/env python
import mincemeat

#using Sieve of Eratosthenes algorithm
#preload primes using algorithm in less than 1 second
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
    
data = [primes1(10000000)]



# The data source can be any dictionary-like object
datasource = dict(enumerate(data))





def mapfn(k, v):
     for num in v:
       if(str(num) == str(num)[::-1]):
          #print num
          yield "Primes", num
          
    	      
   
     	  	
def reducefn(k, vs):
    result = vs
   
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print results
print len(results["Primes"])

