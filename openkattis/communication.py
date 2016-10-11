#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("5\n58 89 205 20 198\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	numbers = map(int,sys.stdin.readline().replace('\n','').split(' '))
	numT = map(str,map(lambda x: trans(x),numbers))
	print " ".join(numT)

def trans(j):
	i=2
	resp = j&1
	while i<=128:
		resp |= (j&i)^((resp&(i/2)) <<1)
		i*=2
	return resp

main()
# stop = timeit.default_timer()

# print stop - start 
	