#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit
# import itertools

# sys.stdin = StringIO.StringIO("3\nMozart\nBeethoven\nBach\n5\nHilbert\nGodel\nPoincare\nRamanujan\nPochhammmer\n0\n")
# start = timeit.default_timer()
def main():
	first = True
	for line in sys.stdin:
		n = int(line.replace('\n',''))
		if n ==0:
			break
		arr = []
		for i in range(n):
			arr.append(sys.stdin.readline().replace('\n',''))
		arr.sort(key=lambda x:x[0:2])
		if not first:
			print ""
		print "\n".join(arr)
		first = False


				
main()
# stop = timeit.default_timer()

# print stop - start 
		