#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("16")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = float(sys.stdin.readline().replace('\n',''))
	print "%.6f"%(math.sqrt(n)*4)


main()
# stop = timeit.default_timer()

# print stop - start 
	