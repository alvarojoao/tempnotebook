#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("3\nSimon says raise your right hand.\nLower your right hand.\nSimon says raise your left hand.\n")
# sys.stdin = StringIO.StringIO("100 5\n42\n3\n2\n99\n1\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for i in range(n):
		line = sys.stdin.readline().replace('\n','')
		if line[:10]=="Simon says":
			print line[10:]


main()
# stop = timeit.default_timer()

# print stop - start 
	