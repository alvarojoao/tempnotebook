#! /usr/bin/python2
from __future__ import division

import sys
import math
from collections import Counter
import StringIO
# import re
# import timeit

sys.stdin = StringIO.StringIO("***\n*.*.*.*.*.*.*.*.*\n*..*.*.*.*.*.*.*.*\n*..*..*\n*\n***\n*.**\nEND\n")#3^4\n15\n9^2
# sys.stdin = StringIO.StringIO("***\nEND\n")#3^4\n15\n9^2

# start = timeit.default_timer()


def main():
	count = 1
	for line in sys.stdin:
		texture = line.replace('\n','').replace(' ','')
		if 'END' in texture.upper():
			break
		firstBlack = 0
		for i,char in enumerate(texture):
			if char=='*':
				firstBlack = i
				break
		lastBlack = 0
		for i,char in enumerate(texture[::-1]):
			if char=='*':
				lastBlack = len(texture)-1-i
				break
		counter = []
		countAny = 0
		for i in range(firstBlack,lastBlack+1):
			if texture[i]=='.':
				countAny+=1

			if i<len(texture)-1 and texture[i+1]=='*':
				break
		isEven =True
		for i in range(firstBlack,lastBlack+1):
			if texture[i] == '*' and not i==lastBlack:
				countDot = 0
				for j in range(i+1,len(texture)):
					if texture[j]=='.':
						countDot+=1
					if texture[j]=='*':
						break
				if not countDot==countAny:
					isEven = False
					break



		if isEven:
			print str(count)+' EVEN'
		else:
			print str(count)+' NOT EVEN'
		count += 1


main()
# stop = timeit.default_timer()

# print stop - start 
	