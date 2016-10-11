#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("2 0 0 2\n4 16 8 2\n2 64 32 4\n1024 1024 64 0\n3\n")
# sys.stdin = StringIO.StringIO("2 0 0 2\n4 16 8 2\n2 64 32 4\n1024 1024 64 0\n1\n")

# start = timeit.default_timer()
def main():
	matrix = []
	for i in range(4):
		line = sys.stdin.readline()
		lineArray = map(int,line.replace('\n','').split(' '))
		matrix.append(lineArray)

	for n in range(len(matrix)):
		print " ".join(map(str,matrix[n]))
	print ""
	n = int(sys.stdin.readline().replace('\n',''))
	if n ==0:
		matrix = moveLeft(matrix)
	elif n ==1:
		matrix = moveUp(matrix)
	elif n ==2:
		matrix = moveRigth(matrix)
	elif n ==3:
		matrix = moveDown(matrix)

	for n in range(len(matrix)):
		print " ".join(map(str,matrix[n]))

def calculate(matrix):
	for i in range(len(matrix)):
		for p in range(len(matrix[i])):
			for j in range(len(matrix[i])-1)[::-1]:
				if matrix[i][j+1]==0:
					matrix[i][j+1]+=matrix[i][j]
					matrix[i][j]= 0

		for j in range(len(matrix[i])-1)[::-1]:
			if matrix[i][j+1]==matrix[i][j]:
				matrix[i][j+1]+=matrix[i][j]
				matrix[i][j]=0

		for p in range(len(matrix[i])):
			for j in range(len(matrix[i])-1)[::-1]:
				if matrix[i][j+1]==0:
					matrix[i][j+1]+=matrix[i][j]
					matrix[i][j]= 0
		


	return matrix

def moveRigth(matrix):
	return calculate(matrix)

def moveLeft(matrix):
	matrix = map(lambda x: x[::-1],matrix)
	matrix = calculate(matrix)
	matrix = map(lambda x: x[::-1],matrix)
	return matrix

def moveDown(matrix):
	matrix = rowToCol(matrix)
	matrix = calculate(matrix)
	matrix = rowToCol(matrix)
	return matrix

def moveUp(matrix):
	matrix = rowToCol(matrix)
	matrix = map(lambda x: x[::-1],matrix)
	matrix = calculate(matrix)
	matrix = map(lambda x: x[::-1],matrix)
	matrix = rowToCol(matrix)
	return matrix

def rowToCol(matrix):
	newMatrix = []
	for i in range(len(matrix)):
		newMatrix.append([])
		for j in range(len(matrix[i])):
			newMatrix[i].append(matrix[j][i])
	return newMatrix

main()
# stop = timeit.default_timer()

# print stop - start 
	