#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("10 12\n71293781758123 72784\n1 12345677654321")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		numbers = line.replace('\n','').split(' ')
		final = 0
		for num in numbers:
			final -= int(num)
			final = abs(final)
		print final

main()
# stop = timeit.default_timer()

# print stop - start 
	