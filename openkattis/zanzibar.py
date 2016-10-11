#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("3\n1 100 0\n1 1 1 2 2 4 8 8 9 0\n1 28 72 0\n")
# sys.stdin = StringIO.StringIO("100 5\n42\n3\n2\n99\n1\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for i in range(n):
		numbers = map(int,sys.stdin.readline().replace('\n','').split(' '))
		maxValue = 0
		for i in range(1,len(numbers)):
			maxValue += max(0,numbers[i] - numbers[i-1]*2)
		print maxValue

main()
# stop = timeit.default_timer()

# print stop - start 
	