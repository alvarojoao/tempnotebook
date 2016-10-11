#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("16")

# sys.stdin = StringIO.StringIO("10 8 6\n15 30\n25 50\n70 80\n")
# start = timeit.default_timer()
def main():
	a,b,c = map(int,sys.stdin.readline().replace('\n','').split(' '))
	arr = [0]*101
	for i in range(3):
		s,f = map(int,sys.stdin.readline().replace('\n','').split(' '))
		for k in range(s,f):
			arr[k]+=1
	total = 0
	for arrv in arr:
		if arrv == 1:
			total +=a
		elif arrv == 2:
			total += b*2
		elif arrv == 3:
			total += c*3

	print total 


main()
# stop = timeit.default_timer()

# print stop - start 
	