#! /usr/bin/python2

import sys
import math
import StringIO
import itertools
# import timeit


sys.stdin = StringIO.StringIO("20\n40 50 60 70 120 130 140 180 190 200 1 2 3 4 5 10 11 12 13 14\n")
# sys.stdin = StringIO.StringIO("4\n50 60 70 120\n")
# sys.stdin = StringIO.StringIO("40\n1 2 3 4 5 10 11 12 13 14 15 16 20 21 22 23 24 30 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 60 70 120\n")

# start = timeit.default_timer()

def main2():
	minWeight = 200
	num = int(sys.stdin.readline().replace('\n',''))
	fruits = sys.stdin.readline().replace('\n','').split(' ')
	valuesFruits = map(int,fruits)
	comb = [ sum(j) for i in range(1,num+1) for j in list(itertools.combinations(valuesFruits,i)) if sum(j)>=minWeight ]
	# print  sum([sum(i) for i in filter(lambda x: sum(x)>=minWeight,comb)])
	print  sum(comb)

main2()
# stop = timeit.default_timer()

# print stop - start 