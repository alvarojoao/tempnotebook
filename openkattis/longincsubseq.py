#! /usr/bin/python2

import sys
import math
import StringIO
# import timeit


sys.stdin = StringIO.StringIO("10\n5 19 5 81 50 28 29 1 83 23\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2

# start = timeit.default_timer()
def main2():
	for line in sys.stdin:
		num = int(line)
		numbers = map(int,sys.stdin.readline().replace('\n','').split(' '))
		maxResult = []
		for i,number in enumerate(numbers):
			solutions = [i]
			for j in range(i+1,len(numbers)):
				if numbers[solutions[-1]]<numbers[j]:
					solutions.append(j)
			if len(solutions)>=len(maxResult):
				maxResult = solutions
		print len(maxResult)
		print " ".join(map(str,maxResult))





main2()
# stop = timeit.default_timer()

# print stop - start 