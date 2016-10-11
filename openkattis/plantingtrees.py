#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit
# sys.stdin = StringIO.StringIO("4\n2 3 4 3\n")
# sys.stdin = StringIO.StringIO("6\n39 38 9 35 39 20\n")

def main():

	n =  int(sys.stdin.readline().replace('\n',''))
	trees =  filter(filterNone,map(maybeInt,sys.stdin.readline().replace('\n','').split(' ')))
	trees.sort(key=int)
	maax = 0
	for i,val in enumerate(trees[::-1]):
		days = i+1+val
		maax = max(maax,days)
	print maax+1

def maybeInt(x):
	if not x == "":
		return int(x)
def filterNone(x):
	if not x==None:
		return True
	else:
		return False
main()