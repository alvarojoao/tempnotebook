#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
import re
# import timeit
# import itertools

# sys.stdin = StringIO.StringIO("dcbagfekjih\nmobitel\nanakonda\n")
# sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\n")
# sys.stdin = StringIO.StringIO("\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		line = line.replace('\n','')
		print "%.16f"%(len(re.findall("_", line))/len(line))
		print "%.16f"%(len(re.findall("[a-z]", line))/len(line))
		print "%.16f"%(len(re.findall("[A-Z]", line))/len(line))
		print "%.16f"%(len(re.findall("[\W\d]", line))/len(line))
				
main()
# stop = timeit.default_timer()

# print stop - start 
		