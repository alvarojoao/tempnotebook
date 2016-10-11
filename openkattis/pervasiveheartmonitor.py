#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit
# sys.stdin = StringIO.StringIO("Lisa Marie Presley 90.2 104.3 110.1 118.7 122.3\n72.2 74 79.5 82.1 88.3 87.4 87.2 88.1 83.8 Bono\n")
# sys.stdin = StringIO.StringIO("6\n39 38 9 35 39 20\n")

def main():
	for line in sys.stdin:
		allvalues =  map(maybeFloat,line.replace('\n','').split(' '))
		numericVal = filter(lambda x: isinstance(x, float),allvalues)
		strVal = " ".join(filter(lambda x: isinstance(x, str),allvalues))

		print "%.6f %s"%((sum(numericVal)/len(numericVal)),strVal)

def maybeFloat(s):
    try: 
        return float(s)
    except ValueError:
        return s

def maybeInt(x):
	if not x == "":
		return int(x)
def filterNone(x):
	if not x==None:
		return True
	else:
		return False
main()