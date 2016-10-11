#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit
# import itertools

# sys.stdin = StringIO.StringIO("1 1\n2 1 -1 1 -1 2\n3 2 -4 8 3 -6 1 4 6 -1 -6 10\n")
# sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\n")
# sys.stdin = StringIO.StringIO("\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		nums = map(maybeInt,line.replace('\n','').split(' '))
		for i in range(len(nums)):
			value = nums.pop(i)
			if value == sum(nums):
				print value
				break
			nums.insert(i,value)
def maybeInt(x):
	if x == "":
		return 0
	else:
		return int(x)

main()
# stop = timeit.default_timer()

# print stop - start 
		