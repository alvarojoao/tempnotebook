#! /usr/bin/python2
from __future__ import division

import sys
import math
from collections import Counter
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("4\n1 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919\n2 919 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900\n3 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 900\n4 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900 919\n")

# start = timeit.default_timer()


def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for line in range(n):
		nuns = map(int,sys.stdin.readline().replace('\n','').split(' '))
		stepsB = 0
		arr = nuns[1:]
		for x in range(len(arr)):
			for y in range(x):
				if arr[x]<arr[y]:
					arr[x], arr[y] = arr[y], arr[x]
					stepsB+= 1
		print nuns[0],stepsB

main()
# stop = timeit.default_timer()

# print stop - start 
	