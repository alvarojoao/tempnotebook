#! /usr/bin/python2
# from __future__ import division

import sys
import math
# import StringIO
# import timeit


# sys.stdin = StringIO.StringIO("10 5 2\n")
# sys.stdin = StringIO.StringIO("5 2 1\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2

# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		b,k,g  = map(int,line.replace('\n','').split(' '))
		group = k/g
		days=0
		while b>1:
			b-=group
			days+=1
		print days






main()
# stop = timeit.default_timer()

# print stop - start 