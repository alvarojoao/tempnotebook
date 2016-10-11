#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
import itertools
# import timeit


# sys.stdin = StringIO.StringIO("4\n900\n500\n498\n4\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	weights = []
	for i in range(n):
		weights.append(int(sys.stdin.readline().replace('\n','')))
	comb = []
	for j in  range(2,3):
		comb.append([k+(sum(k),) for k in itertools.combinations(weights,j)])
	# print comb
	comb = reduce(lambda x,y:x+y ,comb)
	comb.sort(key=lambda x:gaussian(x[-1]-1000,0,0.2))
	print comb[-1][-1]
	# print map(sum, comb)	

	# combs = map(lambda x:x-1000,map(sum, comb))
	# print combs

def gaussian(x, mu, sig):
	return math.exp(-math.pow(x - mu, 2.) / (2 * math.pow(sig, 2.)))

def main2():
	n = int(sys.stdin.readline().replace('\n',''))
	weights = []
	for i in range(n):
		weights.append(int(sys.stdin.readline().replace('\n','')))
	
	gp = [False]*2001
	gp[0] = True
	for w in weights:
		for k in range(2001)[::-1]:
			if k-w >= 0:
				gp[k] |= gp[k-w]
	start = 1000
	for i in range(1000):
		for j in [1,-1]:
			if gp[start + i*j]:
				print start+i*j
				return

main2()
# stop = timeit.default_timer()

# print stop - start 
	