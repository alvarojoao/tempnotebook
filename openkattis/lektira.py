#! /usr/bin/python2

import sys
import math
import StringIO
# import re
# import timeit
import itertools

# sys.stdin = StringIO.StringIO("dcbagfekjih\nmobitel\nanakonda\n")
sys.stdin = StringIO.StringIO("dcbagfekjih\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		s = line.replace('\n','').replace(' ','').lower()
		finalList = []
		for i in range(1,len(s)):
			for j in range(i+1,len(s)):
				finalList.append(splitInvert(s,i,j))

		print sorted(finalList).pop(0)

def splitInvert(s,i,j):
	return s[0:i][::-1]+s[i:j][::-1]+s[j:][::-1]

main()
# stop = timeit.default_timer()

# print stop - start 
	