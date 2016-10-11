#! /usr/bin/python2
# from __future__ import division
import sys
import math
import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("3029\n4\n5\n42\n0\n")
# sys.stdin = StringIO.StringIO("10 250\n")
# sys.stdin = StringIO.StringIO("1\n20 1\n20\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		value = int(line.replace('\n',''))
		if value==0:
			break
		sum10R = sum10(value)
		p = 11
		while sum10(value*p) != sum10R:
			p+=1
		print p

def sum10(i):
	sumVl = 0
	while i > 0:
		sumVl += i % 10
		i /= 10
	return sumVl
main()
# stop = timeit.default_timer()

# print stop - start 
	