#! /usr/bin/python2

import sys
import math
import StringIO
# import re
# import timeit
import itertools

# sys.stdin = StringIO.StringIO("dcbagfekjih\nmobitel\nanakonda\n")
sys.stdin = StringIO.StringIO("dcbagfekjih\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		n = int(line.replace('\n','').replace(' ',''))
		if n==0:
			break

		s = line.replace('\n','')
		


main()
# stop = timeit.default_timer()

# print stop - start 
	