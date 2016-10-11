#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("500 70")

# start = timeit.default_timer()
def main():
	N,M = filter(filterInt,map(maybeInt,sys.stdin.readline().split(' ')))
	print int(math.ceil(N/math.sin(math.radians(M))));


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
	