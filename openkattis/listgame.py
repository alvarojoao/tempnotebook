#! /usr/bin/python2
import sys
import math
import StringIO
# import re
import timeit

sys.stdin = StringIO.StringIO("1099511627776\n")#3^4\n15\n9^2
start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	print counter(n)
div = []
primes = [2, 3, 5, 7,11,13,17,19,23,29, 31]

def divisible(n, p):
	div.append(p)
	return counter( n / p) 
    
def lastPrime(n, p):
    #print n,p,n / p +1
    for x in range(p , n / p +1, 2):
        if n % x == 0:
            return divisible(n,x)
	div.append(n)        
    return len(div)
        
def counter(n):
    if n == 1:
        return len(div)
    for p in primes:
        if n % p == 0:
            return divisible(n, p)
    return lastPrime(n, 37)     

main()
stop = timeit.default_timer()

print stop - start 
	