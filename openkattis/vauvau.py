#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("2 2 3 3\n1 3 4\n")
# start = timeit.default_timer()
def main():
	line1 = sys.stdin.readline().replace('\n','')
	line2 = sys.stdin.readline().replace('\n','')
	dogA1,dogA2,dogB1,dogB2 = map(int,line1.split(' '))
	heros = map(lambda x: int(x)-1,line2.split(' '))


	for hero in heros:
		if hero%(dogA1+dogA2) < dogA1:
			if hero%(dogB1+dogB2) < dogB1:
				print "both"
			else:
				print "one"
		else:
			if hero%(dogB1+dogB2) < dogB1:
				print "one"
			else:
				print "none"


main()
# stop = timeit.default_timer()

# print stop - start 
	