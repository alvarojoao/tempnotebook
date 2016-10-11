#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("5 5\n5 7\n7 5\n")

# start = timeit.default_timer()
def main():
	N= 3
	points = []
	for i in range(N):
		x,y = sys.stdin.readline().replace('\n','').split(" ")
		points.append((x,y))

	if points[0][0] == points[1][0]:
		x4 = points[2][0];
	elif points[0][0] == points[2][0]:
		x4 = points[1][0];
	else:
		x4 = points[0][0];

	if points[0][1] == points[1][1]:
		y4 = points[2][1];
	elif points[0][1] == points[2][1]:
		y4 = points[1][1];
	else:
		y4 = points[0][1];
	print x4,y4

def diff(i,one,two):
	if one[i]==two[i]:
		return "."
	else:
		return "*"
def maybeInt(x):
	if not x.strip()=='':
		return int(x)

def filterInt(x):
	if not x == None:
		return True
	else:
		return False

main()
# stop = timeit.default_timer()

# print stop - start 
	