#! /usr/bin/python2
from __future__ import division
import sys
import math
import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("4\n1 3 2 2\n1 1 3 2\n2 4 7 3\n3 3 5 3\n")
# sys.stdin = StringIO.StringIO("4\n0 0 1 1\n1 2 0 3\n2 2 3 3\n4 0 3 1\n")
# sys.stdin = StringIO.StringIO("3\n4 6 5 5\n2 1 15 1\n3 2 8 7\n")


# sys.stdin = StringIO.StringIO("3\n4 4 4\n")

# start = timeit.default_timer()
class Line:
	def __str__(self):
		return str(self.i)
	def __repr__(self):
		return "%d"%self.i

	def __init__(self,x1,y1,x2,y2,i):
		if x1 != x2:
			self.x1 = min(x1,x2)
			self.y1 = y1 if self.x1 == x1 else y2
			self.x2 = max(x1,x2)
			self.y2 = y2 if self.x2 == x2 else y1
			self.slope  = ((y2-y1)/(x2-x1))
			self.yf = y1-self.slope*x1;
		else:
			self.x1 = x1
			self.y1 = min(y1,y2)
			self.x2 = x2
			self.y2 = max(y1,y2)
			self.slope  = float('inf')
		self.i = i
	def __cmp__(self,other):
		if self.slope == float('inf') or other.slope == float('inf'):
			return min(self.y1, self.y2) - min(other.y1, other.y2);
		elif self.x1 <= other.x1 and self.x2 >= other.x1:
			yF = self.yf + self.slope*other.x1
			if yF > other.y1:
				return 1
			else:
				return -1
		elif self.x1 <= other.x2 and self.x2 >= other.x2:
			yF = self.yf + self.slope*other.x2
			if yF > other.y2:
				return 1
			else:
				return -1
		elif self.x1 >= other.x1 and self.x2 <= other.x2:
			yF = other.yf + other.slope*self.x1
			if yF > self.y1:
				return -1
			else:
				return 1
		else:
			return other.x1 - self.x1



def main():
	N = int(sys.stdin.readline().replace('\n',''))
	allLines = []
	for i in range(1,N+1):
		x1,y1,x2,y2 =  map(int,sys.stdin.readline().replace('\n','').split(' '))
		allLines.append(Line(x1, y1, x2, y2, i))
	allLines = sorted(allLines)
	print " ".join(map(lambda x:str(x.i) ,allLines))



main()
# stop = timeit.default_timer()

# print stop - start 
	