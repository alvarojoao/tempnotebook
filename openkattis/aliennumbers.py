#! /usr/bin/python2
# from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit
# import itertools

# sys.stdin = StringIO.StringIO("4\n9 0123456789 oF8\nFoo oF8 0123456789\n13 0123456789abcdef 01\nCODE O!CDE? A?JM!.\n")
# sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\n")
# sys.stdin = StringIO.StringIO("\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	print n
	for index in range(1,n+1):
		n,s,t = sys.stdin.readline().replace('\n','').split(' ')
		sBase = len(s)
		tBase = len(t)
		result = 0
		for j in range(len(n)):
			result += math.pow(sBase,(len(n)-j-1))*s.index(n[j])
		string = ""
		while(result > 0):
			string += t[int(result % tBase)]
			result /= tBase

		print "Case #%d: %s"%(index, string[::-1]);




main()
# stop = timeit.default_timer()

# print stop - start 
		