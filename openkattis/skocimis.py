#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit
# import itertools

# sys.stdin = StringIO.StringIO("2 3 5")
# sys.stdin = StringIO.StringIO("3 5 9")
# start = timeit.default_timer()
def main():
	a,b,c = map(int,sys.stdin.readline().replace('\n','').split(' '))
	if (b - (a + 1) > c - (b + 1)):
		print "%d"%(b - (a + 1));
	else:
		print "%d"%(c - (b + 1));

main()
# stop = timeit.default_timer()

# print stop - start 
		