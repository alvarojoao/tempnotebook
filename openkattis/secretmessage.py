#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("2\niloveyoutooJill\nTheContestisOver\n")
# sys.stdin = StringIO.StringIO("100 5\n42\n3\n2\n99\n1\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for i in range(n):
		string = sys.stdin.readline().replace('\n','')
		l = len(string)
		while not isPerfectSqrt(l) :
			l+=1
		string += "*"*(l-len(string))
		n = int(math.sqrt(l))
		block = [ [' ' for i in range(n) ] for j in range(n)]
		for i in range(n):
			for j in range(n):
				block[i][j] = string[i*n+j]
		rotacionado = [ [0 for i in range(n) ] for j in range(n)]
		for i in range(n)[::-1]:
			for j in range(n)[::-1]:
				rotacionado[j][i] = block[n-1-i][j]

		# print "".join(rotacionado)
		print reduce(lambda x,y: x+y,map(lambda x:"".join(x).replace('*',''),rotacionado))
		print ''

def isPerfectSqrt(n):
	return math.trunc(math.sqrt(n))==math.sqrt(n)
main()
# stop = timeit.default_timer()

# print stop - start 
	