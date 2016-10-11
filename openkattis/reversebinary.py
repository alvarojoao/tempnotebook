#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("13")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline())
	print int('{0:b}'.format(n)[::-1], 2)


main()
# stop = timeit.default_timer()

# print stop - start 
	