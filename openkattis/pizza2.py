#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("2 1")

# start = timeit.default_timer()
def main():
	N,M = filter(filterInt,map(maybeInt,sys.stdin.readline().split(' ')))
	area = math.pi*(N-M)**2
	areaT = math.pi*(N)**2
	print "%.6f"%((area/areaT)*100)


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
	