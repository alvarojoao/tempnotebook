#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit
# import itertools

# sys.stdin = StringIO.StringIO("2\n10 3\n2 6 7\n214 7\n11 12 7 13\n176 23 191\n")
# start = timeit.default_timer()
def main():
	allLines = []
	for line in sys.stdin:
		allLines += map(int,line.replace('\n','').split(' '))

	iteratorList = iter(list(allLines))


	n = next(iteratorList)

	for i in range(n):
		lex = next(iteratorList)
		num = next(iteratorList)
		arr = []
		minV = -1
		maxV = -1

		for j in range(num):
			arr += [next(iteratorList)]

		for pVal in arr:
			minV = max(minV,min(pVal,lex-pVal))
			maxV = max(maxV,max(pVal,lex-pVal))

		print minV,maxV

				
main()
# stop = timeit.default_timer()

# print stop - start 
		