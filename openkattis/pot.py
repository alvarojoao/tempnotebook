#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("5\n23\n17\n43\n52\n22\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	numbers = []
	for i in range(n):
		numbers.append(sys.stdin.readline().replace('\n',''))
	print sum([ int(n[:-1])**int(n[-1]) for n in numbers ])


main()
# stop = timeit.default_timer()

# print stop - start 
	