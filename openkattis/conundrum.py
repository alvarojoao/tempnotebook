#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("SECRET\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		lineText = line.replace("\n","").upper()
		days = 0
		for i,character in enumerate(lineText.upper()):
			if i%3 == 0 and "P" != character:
				days+=1
			elif i%3 == 1 and "E" != character:
				days+=1
			elif i%3 == 2 and "R" != character:
				days+=1
		print days
main()
# stop = timeit.default_timer()

# print stop - start 
	