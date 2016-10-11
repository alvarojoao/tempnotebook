#! /usr/bin/python2
from __future__ import division
import sys
import math
import StringIO
# import timeit


sys.stdin = StringIO.StringIO("2 4\n1 rock 2 paper\n1 scissors 2 paper\n1 rock 2 rock\n2 rock 1 scissors\n2 1\n1 rock 2 paper\n0\n")
# sys.stdin = StringIO.StringIO("2 4\n1 rock 2 paper\n1 scissors 2 paper\n1 rock 2 rock\n2 rock 1 scissors\n")

# start = timeit.default_timer()
def main():
	first = True
	for line in sys.stdin:
		if line.replace('\n','')=="0":
			break
		n,k = map(int,filter(stringOrInt,line.replace('\n','').split(' ')))
		numOfGames= int(math.ceil(k*n*(n-1)/2))
		win={}
		lost={}
		for i in range(1,n+1):
			win[str(i)]=0
			lost[str(i)]=0

		for j in range(numOfGames):
			game = filter(stringOrInt,sys.stdin.readline().replace('\n','').split(' '))
			player1 = game[0]
			move1 = game[1]
			player2 = game[2]
			move2 =  game[3]
			calc = calculate(move1.lower(),move2.lower())
			if calc>0:
				win[player1]+=1
				lost[player2]+=1
			elif calc==0:
				pass
			else:
				win[player2]+=1
				lost[player1]+=1
		if not first:
			print ""
		first = False
		for k in range(1,n+1):
			if win[str(k)]+lost[str(k)]==0:
				print "-"
			else:
				print "%.3f"%(win[str(k)]/(win[str(k)]+lost[str(k)]))






def calculate(x,y):
	if x=="rock":
		if y=="paper":
			return -1
		elif y=="rock":
			return 0
		else:
			return 1
	elif x=="paper":
		if y=="scissors":
			return -1
		elif y=="paper":
			return 0
		else:
			return 1
	elif x=="scissors":
		if y=="rock":
			return -1
		elif y=="scissors":
			return 0
		else:
			return 1
	return None



def stringOrInt(x):
	if x=="":
		return False
	else:
		return True



main()
# stop = timeit.default_timer()

# print stop - start 