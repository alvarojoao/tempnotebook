#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("9\n0 1 1 1 0 0 0 0 0\n1 0 0 0 0 0 1 0 0\n1 0 0 1 0 1 0 0 0\n1 0 1 0 0 1 1 0 0\n0 0 0 0 0 0 1 1 0\n0 0 1 1 0 0 0 0 0\n0 1 0 1 1 0 0 1 0\n0 0 0 0 1 0 1 0 1\n0 0 0 0 0 0 0 1 0\n1\n0\n-1\n")

# start = timeit.default_timer()
def main():
	while True:
		n = int(sys.stdin.readline().replace('\n',''))
		if n <0:
			break
		graph = []
		for i in range(n):
			line = sys.stdin.readline().replace('\n','').split(' ')
			graph.append(line)
		weak = []
		for i in range(n):
			neibors = [index for index,v in enumerate(graph[i]) if v == "1"]
			isWeak = True
			for n in neibors:
				neiborsOfNeibors = [index for index,v in enumerate(graph[n]) if v == "1"]
				btw = [nOfn for nOfn in neiborsOfNeibors if nOfn in neibors ]
				if len(btw)>0:
					isWeak = False
					break
			if isWeak:
				weak.append(i)
		print " ".join(map(str,weak))



main()
# stop = timeit.default_timer()

# print stop - start 
	