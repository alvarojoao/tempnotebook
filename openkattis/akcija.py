#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("6\n6\n4\n5\n5\n5\n5\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	allBooks = []
	for i in range(n):
		allBooks.append(int(sys.stdin.readline().replace('\n','')))
	allBooks.sort(key=int,reverse=True)
	print sum([ price for i,price in enumerate(allBooks) if not (i+1)%3==0 ])


main()
# stop = timeit.default_timer()

# print stop - start 
	