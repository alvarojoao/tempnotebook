#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("3\n3\n1 2147483647 2147483647\n5\n3 4 7 4 3\n5\n2 10 2 10 5\n")
# sys.stdin = StringIO.StringIO("100 5\n42\n3\n2\n99\n1\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for c in range(n):
		d = dict()
		nguess = int(sys.stdin.readline().replace('\n',''))
		guess = map(int,sys.stdin.readline().replace('\n','').split(' '))
		for i in guess:
			if d.get(i,0) == 0:
				d[i] = i
			elif d.get(i,0) == i:
				del d[i]
		print "Case #%d: %d"%(c+1,map(int,d)[0])


main()
# stop = timeit.default_timer()

# print stop - start 
	