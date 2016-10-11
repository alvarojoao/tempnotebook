#! /usr/bin/python2

import sys
import math
# import StringIO
import itertools
# import timeit


# sys.stdin = StringIO.StringIO("3\n5 1 2 3 4 5\n3 20 6 13\n4 5 9 15 19\n")
# sys.stdin = StringIO.StringIO("100 100 1 1 1\n200 100 5 3 4\n201 132 48 1900 156\n0 0 0 0 0\n")
# sys.stdin = StringIO.StringIO("40\n1 2 3 4 5 10 11 12 13 14 15 16 20 21 22 23 24 30 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 60 70 120\n")

# start = timeit.default_timer()

def main():
	n = int(sys.stdin.readline())
	for i in range(n):
		line = sys.stdin.readline().replace('\n','')
		numbers = map(int,line.split(' '))[1:]
		diff = list(set([numbers[i]-numbers[i+1] for i in range(len(numbers)-1)]))
		numbers.sort(key=int)
		diff2 = list(set([numbers[i]-numbers[i+1] for i in range(len(numbers)-1)]))
		if len(diff)==1:
			print "arithmetic"
		elif len(diff2)==1:
			print "permuted arithmetic"
		else:
			print "non-arithmetic"

main	()
# stop = timeit.default_timer()

# print stop - start 