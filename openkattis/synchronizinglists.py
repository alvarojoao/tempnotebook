#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("4\n10\n67\n68\n28\n55\n73\n10\n6\n7\n98\n23\n61\n49\n1\n79\n9\n1\n15\n32\n47\n68\n39\n24\n0\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	for num in sys.stdin:
		num = int(num)
		if num == 0:
			break
		firstList = []
		secondList = []
		for i in range(0,num):
			number = sys.stdin.readline().replace('\n','')
			firstList.append(int(number))

		for i in range(0,num):
			number = sys.stdin.readline().replace('\n','')
			secondList.append(int(number))
		
		firstListSorted = sorted(firstList)
		secondListSorted = sorted(secondList)
		relation = [ (firstListSorted[i],secondListSorted[i]) for i in range(0,len(firstListSorted)) ]
		for number in firstList:
			print [ sec for first,sec in relation if first==number][0]
		print ""
			
main()
# stop = timeit.default_timer()

# print stop - start 
	