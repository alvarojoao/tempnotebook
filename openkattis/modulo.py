#! /usr/bin/python2
from __future__ import division

import sys
import math
from collections import Counter
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")#3^4\n15\n9^2

# start = timeit.default_timer()


def main():
	numbers = []
	for line in sys.stdin:
		num = int(line.replace('\n',''))
		numbers.append(num)
	modulo = list(set(map(lambda x:x%42,numbers)))
	print len(modulo)
main()
# stop = timeit.default_timer()

# print stop - start 
	