#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit
# import itertools

# sys.stdin = StringIO.StringIO("3\n7\n9901\n")
# start = timeit.default_timer()

def calc(number):
	# ones = int("1"*len(str(number)))
	ones = 1
	count = 1
	countRev = number
	onesRev = int("1"*len(str(number)))

	while (number>1 and number%2!=0 and number%5!=0) and (ones%number != 0):
		if  onesRev%number == 0 :
			count = countRev
			break
		count+=1
		countRev -= 1
		ones=int(str(ones)+"1")
		onesRev = int("1"*len(str(countRev)))
	return count

def main2():
	maxV = -1
	minV = 1
	for i in range(2000):
		start = timeit.default_timer()
		count = calc(i)
		maxV = max(-1,max(maxV,count))
		minV = max(1,min(minV,count))
		print i,count
		stop = timeit.default_timer()
		print stop - start 
	print maxV,minV
def main():
	for line in sys.stdin:
		number  = int(line.replace('\n',''))
		print calc(number)
	
main()

# stop = timeit.default_timer()
# print stop - start 

		