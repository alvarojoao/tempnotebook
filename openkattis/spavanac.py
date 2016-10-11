#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("0 30")

# start = timeit.default_timer()
def main():
	H,M = filter(filterInt,map(maybeInt,sys.stdin.readline().split(' ')))
	if M-45 < 0:
		if H-1<0:
			H = 23
		else:
			H-=1
		M = 60 + (M-45)
	else:
		M -= 45
	print H,M


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
	