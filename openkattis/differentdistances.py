#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

			
# sys.stdin = StringIO.StringIO("1.0 1.0 2.0 2.0 2.0\n1.0 1.0 2.0 2.0 1.0\n1.0 1.0 20.0 20.0 10.0\n0\n")
# sys.stdin = StringIO.StringIO("2 0 0 2\n4 16 8 2\n2 64 32 4\n1024 1024 64 0\n1\n")

# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		numbers = line.replace('\n','')
		if len(numbers.split(' '))<=2:
			break

		x1,y1,x2,y2,p = map(float,numbers.split(' '))

		distance = math.pow(math.pow(abs(x1-x2),p)+math.pow(abs(y1-y2),p),1/p)
		print "%.10f" % distance


main()
# stop = timeit.default_timer()

# print stop - start 
	