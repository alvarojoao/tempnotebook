#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("4\n1 0 0 1 1 2 2 1 1 0 1 2 0\n2 0 1 2 4 3 1 3 4 5 2 1 0\n3 0 1 2 4 4 1 0 2 4 1 0 0\n4 0 1 2 3 4 5 6 7 8 9 10 0\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	num = sys.stdin.readline()
	num = int(num)
	for i in range(1,num+1):
		string = sys.stdin.readline()
		numbers = string.replace('\n','').split(' ')
		numbers = map(int,numbers[1:])
		count = 0
		for j in range(1,len(numbers)-1):
			for k in range(j,len(numbers)-1):
				if isIsland(j,k,numbers):
					count+=1

		print i,count

def isIsland(i,j,numbers):
	for index in range(i,j+1):
		if(numbers[index]<=numbers[i-1] or numbers[index]<= numbers[j+1]):
			return False
	return True
main()
# stop = timeit.default_timer()

# print stop - start 
	