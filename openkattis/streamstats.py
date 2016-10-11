#! /usr/bin/python2
from __future__ import division
from decimal import *
import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("5\n1325338338022 320412 160\n1325338361231 441201 320\n1325338341231 474123 96\n1325338312302 234123 312\n1325338331141 623132 147\n5\n1325300000000 1325400000000\n1325338300000 1325338500000\n1325338336412 1325338339612\n1325338312302 1325338341231\n1325338320000 1325338340000\n")

class Point:
	def __init__(self,point,duration=0,taxa=0,outPutFinal=False,query=False,initialPoint=None):
		self.point = point
		self.duration = duration
		self.taxa = taxa
		self.query = query
		self.outPutFinal = outPutFinal
		self.total = 0
		self.answer = 0
		self.initialPoint = initialPoint
	def __str__(self):
 		return " ".join(map(str,[self.point,self.duration,self.taxa,self.outPutFinal,self.query]))
	def __repr__(self):
 		return " ".join(map(str,[self.point,self.duration,self.taxa,self.outPutFinal,self.query]))

def main():
	n = int(sys.stdin.readline())
	allPoints = []
	for i in range(n):
		t,d,i = filter(lambda x:not x==None,map( maybeInt, sys.stdin.readline().split(' ')))
		all	s.append(Point(t-d,d,i))
		allPoints.append(Point(t,d,i,True,False,allPoints[-1]))
	
	q = int(sys.stdin.readline())
	outputs = []
	for i in range(q):
		line = sys.stdin.readline()
		ini,fin = filter(lambda x:not x==None,map( maybeInt, line.split(' ')))
		allPoints.append(Point(ini,0,0,False,True))
		allPoints.append(Point(fin,0,0,True,True,allPoints[-1]))
		outputs.append(allPoints[-1])
	allPoints.sort(key=lambda p:p.point)
	taxa = 0
	before = None
	for i,point in enumerate(allPoints):
		if not before ==None:
			total=taxa*(abs(before.point-point.point))
			point.total = total+before.total
		before = point
		if point.query and point.outPutFinal:
			point.answer=(point.total-point.initialPoint.total)/1000
	
		if not point.query and not point.outPutFinal:
			taxa+=point.taxa
		elif not point.query and point.outPutFinal:
			taxa-=point.taxa
	for output in outputs:
		print "%.3f"%(output.answer)


def maybeInt(x):
	if not x.strip()=='':
		return int(x)

main()
# stop = timeit.default_timer()

# print stop - start 
	