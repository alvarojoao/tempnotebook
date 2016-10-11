#! /usr/bin/python2
from __future__ import division
import sys
import math
import StringIO
# import re
# import timeit
# import itertools

sys.stdin = StringIO.StringIO("at\nordeals\nabcdefghijklmnopqrstuvwxyz\nabcdefghijklmabcdefghijklm\nabcdABCDabcd\n")
# sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\n")
# sys.stdin = StringIO.StringIO("\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		line = list(set(line.replace('\n','')))
		print "%d"%(2*(len(line))**(len(line)-2))
				
main()
# stop = timeit.default_timer()

# print stop - start 
		