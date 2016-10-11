#! /usr/bin/python2
import sys
import math
import StringIO
import re
import timeit

# sys.stdin = StringIO.StringIO("2\n\n5\n5\n2\n7\n3\n8\n\n6\n7\n11\n2\n7\n3\n4\n")
# start = timeit.default_timer()
def main():
	N = int(sys.stdin.readline().replace('\n',''))
	for line in sys.stdin:
		line = line.replace('\n','')
		if line == '':
			continue

		nC = int(line)
		if nC==0:
			break
		candies = 0
		for i in range(nC):
			line2 = sys.stdin.readline()
			nLong = int(line2.replace('\n',''))
			candies = (candies + nLong % nC) % nC

		if candies == 0:
			print "YES"
		else:
			print "NO"
main()
# stop = timeit.default_timer()

# print stop - start 
	