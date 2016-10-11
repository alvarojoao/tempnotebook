#! /usr/bin/python2
from __future__ import division

import sys
import math
from collections import Counter
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("27 12\n2460000 98400\n3 4000\n0 0\n")#3^4\n15\n9^2

# start = timeit.default_timer()


def main():
	for line in sys.stdin:
		numbers = line.replace('\n','').split(' ')
		
		numerator = int(numbers[0])
		denominator = int(numbers[1])
		if denominator==0 and numerator==0:
			break
		string  = str(int(math.floor(numerator/denominator)))+' '+str(numerator%denominator)+' / '+str(denominator)
		print string
main()
# stop = timeit.default_timer()

# print stop - start 
	