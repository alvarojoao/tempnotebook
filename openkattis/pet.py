#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("5 4 4 5\n5 4 4 4\n5 5 4 4\n5 5 5 4\n4 4 4 5\n")
# start = timeit.default_timer()
def main():
	notes = []
	for line in sys.stdin:
		sumUp = sum(map(int,line.replace('\n','').split(' ')))
		notes.append(sumUp)
	value = max(notes)
	print (notes.index(value)+1),value


main()
# stop = timeit.default_timer()

# print stop - start 
	