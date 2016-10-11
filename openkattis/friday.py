#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit

sys.stdin = StringIO.StringIO("3\n20 1\n20\n40 2\n21 19\n365 12\n31 28 31 30 31 30 31 31 30 31 30 31\n")
# sys.stdin = StringIO.StringIO("1\n20 1\n20\n")
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for i in range(n):
		D,M = sys.stdin.readline().replace('\n','').split(' ')
		d = map(int,sys.stdin.readline().replace('\n','').split(' '))
		totalDays = 0
		count = 0
		for diasMes in d:
			for i in range(1,diasMes+1):
				if (totalDays+i)%7 == 6 and i==13:
					count+=1
			totalDays+=diasMes
		print count


		

main()
# stop = timeit.default_timer()

# print stop - start 
	