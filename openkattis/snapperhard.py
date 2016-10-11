#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("4\n1 0\n1 1\n4 0\n4 47\n")
# start = timeit.default_timer()
def main():
	num = int(sys.stdin.readline().replace('\n',''))
	for i in range(1,num+1):
		snapper, clicks = map(int,sys.stdin.readline().replace('\n','').split(' '))
		module = 2**snapper
		bulbOn = clicks%module==module-1:

		print "Case #%d: %s"%(i,"ON" if bulbOn else "OFF")
main()
# stop = timeit.default_timer()

# print stop - start 
	