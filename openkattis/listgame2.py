#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("127381\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	i = 0
	arr = [1]
	while(i<=n):
		if n%(i+1) == 0 and  (i+1) not in arr and arr[-1]<(i+1):
			arr.append((i+1))
			n /=(i+1)
			i=0
		i+=1 
	arr = list(set([i for i in map(lambda x:x-1,arr) if i>0]))
	print len(arr)

main()
# stop = timeit.default_timer()

# print stop - start 