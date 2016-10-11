#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("2\n\n1 1\n1\n1\n\n3 2\n1 3 2\n5 5\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for i in range(n):
		blank = sys.stdin.readline()
		ng,nm = map(int,sys.stdin.readline().replace('\n','').split(' '))
		NgArray = map(int,sys.stdin.readline().replace('\n','').split(' '))
		NmArray = map(int,sys.stdin.readline().replace('\n','').split(' '))
		NgArray.sort(key=int)
		NmArray.sort(key=int)

		while(True):
			if len(NgArray)==0 or len(NmArray)==0:
				break
			if NgArray[0]>=NmArray[0]:
				NmArray.pop(0)
			else:
				NgArray.pop(0)


		if len(NgArray)>len(NmArray):
			print "Godzilla"
		else:
			print "MechaGodzilla"


main()
# stop = timeit.default_timer()

# print stop - start 
	