#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit
# sys.stdin = StringIO.StringIO("3\n20 2\n30 6\n10 7\n2\n60 1\n30 5\n4\n15 1\n25 2\n30 3\n10 5\n-1\n")
# sys.stdin = StringIO.StringIO("6\n39 38 9 35 39 20\n")

def main():
	for line in sys.stdin:
		n =  int(line.replace('\n',''))
		if n == -1:
			break
		total = 0
		anterior = 0
		for i in range(n):
			values =  filter(filterNone,map(maybeInt,sys.stdin.readline().replace('\n','').split(' ')))
			total += reduce(lambda x,y:x*(y-anterior),values)
			anterior = values[1]
		print "%d miles"%total

def maybeInt(x):
	if not x == "":
		return int(x)
def filterNone(x):
	if not x==None:
		return True
	else:
		return False
main()