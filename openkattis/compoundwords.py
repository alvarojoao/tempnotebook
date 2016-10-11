#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("a bb\nab b\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	wordsAll = []
	for line in sys.stdin:
		words = line.replace('\n','').split(' ')
		wordsAll += words
	comp = list(set([ word1+word2 for word1 in wordsAll for word2 in wordsAll if word1!= word2  ]))
	comp.sort(key=str)
	print "\n".join(comp)

main()
# stop = timeit.default_timer()

# print stop - start 
	