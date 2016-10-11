#! /usr/bin/python2

import sys
import StringIO
# import timeit
# sys.stdin = StringIO.StringIO("LLLLLRRRRRLLLLLRRRRRLLLLLRRRRRLLLLL")

# start = timeit.default_timer()
def truthtable(n):
  if n < 1:
    return [[]]
  subtable = truthtable(n-1)
  return [ row + [v] for row in subtable for v in ["L","R","P"] ]


def evaluateString(line,initial=1):
	for letter in line:
		if letter =="L":
			initial = initial*2
		elif letter =="R":
			initial = initial*2+1
	return initial


def main():

	for line in sys.stdin:
		total = 0
		maxStar = maxStarFunction(line)
		print maxStar
		if maxStar>0:
			for star in reversed(range(1,maxStar+1)):
			 	strStar = "".join(["".join("*") for i in range(star)])
			 	if strStar in line:

					lines = [line.replace(strStar,re) for re in (map(lambda x:"".join(x),truthtable(star)))]
					print lines
					
					for string in lines:
						total += evaluateString(string)
		else:
			total += evaluateString(line)
		print total


def maxStarFunction(line):
	star = 0
	maxStar = 0
	for i,letter in enumerate(line):
		if letter != "*":
			maxStar = star
			star = 0
		elif letter == "*":
			star += 1
			if i==(len(line)-1):
				maxStar = star
	return maxStar
main()

# stop = timeit.default_timer()

# print stop - start 
