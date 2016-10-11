#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("1\ntoot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot\ndog goes woof\nfish goes blub\nelephant goes toot\nseal goes ow\nwhat does the fox say?\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline())
	for i in range(n):
		sounds = sys.stdin.readline().replace('\n','').split(' ')
		animals = []
		for line in sys.stdin:
			line = line.replace('\n','')
			if line == "what does the fox say?":
				break
			animals.append(line.split(' goes ')[1])
		print " ".join(filter(lambda x: not x in animals, sounds))

main()
# stop = timeit.default_timer()

# print stop - start 
	