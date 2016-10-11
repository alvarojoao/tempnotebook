#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("abcd\naaaa\nababab\n.\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		s = line.replace('\n','')
		if s == '.':
			break
		print checkMultiples(findMultiples(s),s)

def findMultiples(s):
	t = len(s)
	return [i for i in range(1,t/2+1) if t%i==0 ]

def checkMultiples(multi,s):
	for i in multi:
		if (s[0:i]*(len(s)/len(s[0:i]))).startswith(s):
			return (len(s)/len(s[0:i]))
	return 1

main()
# stop = timeit.default_timer()

# print stop - start 
	