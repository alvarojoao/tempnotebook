#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("5\n9\n0\n7\n11\n24\n")

# start = timeit.default_timer()
ops = ['+','-','/','*']

def main():
	ns = int(sys.stdin.readline())
	for i in range(ns):
		n = int(sys.stdin.readline())
		print forLoops(n)
		

def forLoops(n):
	for first in ops:
		for second in ops:
			for thrid in ops:
				string = '4 '+first+' 4 '+second+' 4 '+thrid+' 4'
				if eval(string)==n:
					return string+' = '+str(n)
	return 'no solution'
					


main()
# stop = timeit.default_timer()

# print stop - start 
	