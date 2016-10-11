#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit
# import itertools

sys.stdin = StringIO.StringIO("3\nThe quick brown fox jumps over the lazy dog.\nZYXW, vu TSR Ponm lkj ihgfd CBA.\n.abcde,?abcde!'\" 92384  FGHIJ\n")
# sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\n")
# sys.stdin = StringIO.StringIO("\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	num = int(sys.stdin.readline().replace('\n',''))
	for i in range(num):
		allV=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		line = sys.stdin.readline().replace('\n','').upper()

		for chart in line:
			if chart in allV:
				allV.remove(chart)
		if len(allV)==0:
			print "pangram"
		else:
			allV.sort(key=str)
			print "missing","".join(map(str.lower,allV))


main()
# stop = timeit.default_timer()

# print stop - start 
		