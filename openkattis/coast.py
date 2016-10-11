#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("5 6\n111111\n111111\n100001\n111111\n111111\n")
# sys.stdin = StringIO.StringIO("5 6\n011110\n010110\n111000\n000010\n000000\n")

# start = timeit.default_timer()
def main():
	N,M = filter(filterInt,map(maybeInt,sys.stdin.readline().split(' ')))
	mapCoast = []
	marked = []
	mapCoast.append([0]*(M+2))
	marked.append([0]*(M+2))
	total = 0
	for line in sys.stdin:
		marked.append([0]*(M+2))
		mapCoast.append([0]*1+map(int,line.replace("\n","").replace(" ","").strip())+[0]*1)
	mapCoast.append([0]*(M+2))
	marked.append([0]*(M+2))
	stack = [(0,0)]
	while len(stack)>0:
		x,y = stack.pop()
		for dx,dy in [(x,y-1),(x-1,y),(x,y+1),(x+1,y)]:
			if dx>=0 and dy>=0 and dx<(N+2) and dy<(M+2):
				if mapCoast[dx][dy]==0:
					if marked[dx][dy]==0:
						stack.append((dx,dy))
						marked[dx][dy] = 1
				elif mapCoast[dx][dy]==1:
			 		total+=1
	print total


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
	