#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("3 3\n2\n3\n1\n")
# sys.stdin = StringIO.StringIO("100 5\n42\n3\n2\n99\n1\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	r,n = sys.stdin.readline().replace('\n','').split(' ')
	rooms = []
	if int(r)==int(n):
		print 'too late'
	else:
		for line in sys.stdin:
			rooms.append(int(line.replace('\n','')))
		for i in range(1,int(r)+1):
			if i not in rooms:
				print i
				break




main()
# stop = timeit.default_timer()

# print stop - start 
	