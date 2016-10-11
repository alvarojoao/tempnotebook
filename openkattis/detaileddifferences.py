#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("3\nATCCGCTTAGAGGGATT\nGTCCGTTTAGAAGGTTT\nabcdefghijklmnopqrstuvwxyz\nbcdefghijklmnopqrstuvwxyza\nabcdefghijklmnopqrstuvwxyz0123456789\nabcdefghijklmnopqrstuvwxyz0123456789\n")

# start = timeit.default_timer()
def main():
	N= int(sys.stdin.readline())
	for i in range(N):
		one= sys.stdin.readline().replace('\n','')
		two = sys.stdin.readline().replace('\n','')
		print one
		print two
		print "".join(map(lambda (i,x):diff(i,one,two),enumerate(one)))
		print ""

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
	