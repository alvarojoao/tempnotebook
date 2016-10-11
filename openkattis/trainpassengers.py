#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("1 2\n0 1 1\n1 0 0\n")
# sys.stdin = StringIO.StringIO("10 250\n")
# sys.stdin = StringIO.StringIO("1\n20 1\n20\n")
# start = timeit.default_timer()
def main():
	c,n = map(int,sys.stdin.readline().replace('\n','').split(' '))
	cur = 0
	possible = True
	for i in range(n):
		off,on,left = map(int,sys.stdin.readline().replace('\n','').split(' '))
		cur-=off
		cur+=on
		if cur > c or cur < 0 or cur < c and left > 0 or i == n-1 and (left > 0 or on > 0):
			possible = False
			break

	if possible and cur == 0:
		print "possible"
	else:
		print "impossible"


main()
# stop = timeit.default_timer()

# print stop - start 
	