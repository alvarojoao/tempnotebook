#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("9\nAAAABBBBB")#3^4\n15\n9^2
# start = timeit.default_timer()
Adrian  = "ABC"
Bruno  = "BABC"
Goran  = "CCAABB"
def main():
	num = sys.stdin.readline()
	num = int(num)
	string = sys.stdin.readline()
	AdrianAns = (score(fixLen(Adrian,string),string),"Adrian")
	BrunoAns = (score(fixLen(Bruno,string),string),"Bruno")
	GoranAns = (score(fixLen(Goran,string),string),"Goran")
	maxResult= max([AdrianAns[0],BrunoAns[0],GoranAns[0]])
	print maxResult
	for val,name in [AdrianAns,BrunoAns,GoranAns]:
		if val== maxResult:
			print name

def score(patter,string):
	return sum([1 for i,character in enumerate(string)  if patter[i]==string[i]])
def fixLen(patter,string):
	return (patter*(int(math.ceil(len(string)/len(patter)))))[0:len(string)]

main()
# stop = timeit.default_timer()

# print stop - start 
	