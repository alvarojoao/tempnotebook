#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit

sys.stdin = StringIO.StringIO("7\nBo\nPat\nJean\nKevin\nClaude\nWilliam\nMarybeth\n6\nJim\nBen\nZoe\nJoey\nFrederick\nAnnabelle\n5\nJohn\nBill\nFran\nStan\nCece\n0\n")
# start = timeit.default_timer()
def main():
	count = 1
	for line in sys.stdin:
		n = int(line.replace('\n',''))
		if n==0:
			break
		allString = []
		for i in range(n):
			allString.append(sys.stdin.readline().replace('\n',''))
		allString.sort(key=len)	
		first = [string for i,string in enumerate(allString) if i%2==0]
		second = [string for i,string in enumerate(allString) if not i%2==0]
		second.sort(key=lambda x: (len(x),str(x)),reverse=True)
		print "SET %d"%count
		print "\n".join(first)
		print "\n".join(second)
		count +=1

main()
# stop = timeit.default_timer()

# print stop - start 
	