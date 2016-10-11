#! /usr/bin/python2
# from __future__ import division
import sys
# import math
# import StringIO
# import re
# import timeit
# import itertools
D = 'D'
U = 'U'
# sys.stdin = StringIO.StringIO("UUUDDUDU\n")
# start = timeit.default_timer()
def main():
	line = sys.stdin.readline().replace('\n','')
	up = 1 if line[0] == D else (2 if line[1]== D  else 0)
	down= 1 if line[0] == U else ( 2 if line[1]== U  else 0)
	change =  1 if not line[0] == line[1] else 0
	for index in range(2,len(line)):
		if line[index] == D:
			up+=2
		else:
			down+=2
		if not line[index] == line[index-1]:
			change +=1
	print "\n".join(map(str,[up,down,change]))

main()
# stop = timeit.default_timer()

# print stop - start 
		