#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("6\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		n = int(line.replace('\n',''))
		dots = 1
		for i in range(0,4):
			dots *= (n-i)
			dots /= (i+1)

		print "%.0f" % dots


main()
# stop = timeit.default_timer()

# print stop - start 
	