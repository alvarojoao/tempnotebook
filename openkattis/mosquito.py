#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("10 20 40 4 2 2 10\n144 55 8 0 1 9 4\n10 10 10 2 3 2 6\n10 20 40 86 9 9 999\n")

# sys.stdin = StringIO.StringIO("10 8 6\n15 30\n25 50\n70 80\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		m,a,b,c,d,e,f = map(int,line.replace('\n','').split(' '))
		for i in range(f):
			h = a/e
			a = b/d
			b = m*c
			m = h

		print m


main()
# stop = timeit.default_timer()

# print stop - start 
	