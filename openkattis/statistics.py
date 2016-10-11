#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("2 4 10\n9 2 5 6 4 5 9 2 1 4\n7 6 10 1 2 5 10 9\n1 9\n")

# start = timeit.default_timer()
def main():
	i = 1
	for line in sys.stdin:
		numbers = filter(filterInt,map(maybeInt,line.replace('\n','').split(' ')))[1:]
		minV = min(numbers)
		maxV = max(numbers)
		print "Case %d: %d %d %d"%(i,minV,maxV,abs(minV-maxV))
		i+=1


def maybeInt(x):
	if not x.strip()=='':
		return int(x)

def filterInt(x):
	if not x == None:
		return True
	else:
		return False

main()
# stop = timeit.default_timer()

# print stop - start 
	