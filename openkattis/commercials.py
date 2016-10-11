#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("6 20\n18 35 6 80 15 21\n")

# start = timeit.default_timer()
def main():
	N,P = filter(lambda x: not x==None,map(maybeInt,sys.stdin.readline().split(' ')))
	ns = filter(lambda x: not x==None,map(maybeInt,sys.stdin.readline().split(' ')))
	local = 0
	globalBest = 0
	for n in ns:
		local += n-P
		if local<0:
			local=0
		globalBest = max(globalBest,local)
	print globalBest


def maybeInt(x):
	if not x.strip()=='':
		return int(x)


main()
# stop = timeit.default_timer()

# print stop - start 
	