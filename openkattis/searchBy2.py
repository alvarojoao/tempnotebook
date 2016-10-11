#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit

sys.stdin = StringIO.StringIO("6\n6 7 8 9 10 11\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	allNums = map(int,sys.stdin.readline().replace('\n','').split(" "))
	allnumswithIndex = zip(allNums,xrange(0,len(allNums)))
	search = 8
	resposta = None
	countSteps = 0	
	while(True):
		countSteps+=1
		i = len(allnumswithIndex)/2
		if len(allnumswithIndex) == 0:
			resposta = -1
			break
		if allnumswithIndex[i][0] == search:
			resposta = allnumswithIndex[i][1]
			break 
		elif allnumswithIndex[i][0] < search:
			allnumswithIndex = allnumswithIndex[i:]
		elif allnumswithIndex[i][0] > search:
			allnumswithIndex = allnumswithIndex[:i]

	print resposta,countSteps

main()
# stop = timeit.default_timer()

# print stop - start 
	