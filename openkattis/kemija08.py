#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("zepelepenapa papapripikapa\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	lines = sys.stdin.readline().replace('\n','').split(' ')
	newLines = []
	for line  in lines:
		newLine = ""
		i=0
		while i< len(line):
			if line[i] in "aeiou":
				newLine+=line[i]
				i+=3	
			else:
				newLine+=line[i]
				i+=1
		newLines.append(newLine)
	print " ".join(newLines)



main()
# stop = timeit.default_timer()

# print stop - start 
	