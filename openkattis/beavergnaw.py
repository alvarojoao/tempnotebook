#! /usr/bin/python2
from __future__ import division
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("10 250\n20 2500\n25 7000\n50 50000\n0 0\n")
# sys.stdin = StringIO.StringIO("10 250\n")
# sys.stdin = StringIO.StringIO("1\n20 1\n20\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		D,V = map(int,line.replace('\n','').split(' '))
		if D==0 and V == 0:
			break
		smalld = 0
		ceil = D
		floor = 0
		while(True):
			smalld = (ceil+floor)/2
			volumeAtual = calculateVolume(D,smalld)
			if abs(V-volumeAtual)<1e-6:
				break
		 	
		 	if volumeAtual >= V :
				floor = smalld;
			else:
				ceil = smalld;

		print "%.9f"%smalld


		
def calculateVolume(D,smalld):
	return math.pi*((D**3)/6-(smalld**3)/6)

main()
# stop = timeit.default_timer()

# print stop - start 
	