#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("1\n5\n20 T\n50 T\n80 T\n50 T\n30 T\n")

# start = timeit.default_timer()
def main():
	x = int(sys.stdin.readline().replace('\n',''))-1
	y = int(sys.stdin.readline().replace('\n',''))
	currTime = 210
	for i in range(y):
		value,letter = sys.stdin.readline().replace('\n','').split(' ')
		currTime -= int(value)
		if currTime <= 0:
			break
		if letter == 'T':
			x+=1
			x = x % 8
	print x+1

main()
# stop = timeit.default_timer()

# print stop - start 
	