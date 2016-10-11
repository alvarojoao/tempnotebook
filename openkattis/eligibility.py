#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("3\nEligibleContestant 2013/09/01 1995/03/12 10\nIneligibleContestant 2009/09/01 1990/12/12 50\nPetitionContestant 2009/09/01 1990/12/12 35\n")
# sys.stdin = StringIO.StringIO("5 6\n011110\n010110\n111000\n000010\n000000\n")

# start = timeit.default_timer()
def main():
	N= int(sys.stdin.readline())
	for i in range(N):
		name,dateI,dateO,courses = sys.stdin.readline().replace('\n','').split(' ')
		if int(dateI[:4]) >= 2010 or int(dateO[:4]) >= 1991:
			print "%s eligible"%name
		elif int(courses) > 40:
			print "%s ineligible"%name
		else:
			print "%s coach petitions"%name


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
	