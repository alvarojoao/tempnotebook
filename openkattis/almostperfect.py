#! /usr/bin/python2
from __future__ import division
import sys
import math
import StringIO
import re
import timeit

# sys.stdin = StringIO.StringIO("6\n65\n650\n")
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		num = int(line.replace('\n',''))
		val = 1
		sqrt_ = math.sqrt(num)
		for i in range(2,int(sqrt_)+1):
			if num%i==0:
				val +=i
				val += int(num/i)

		if sqrt_ == int(sqrt_):
			val -= sqrt_

		if val == num:
			print "%d perfect"%num
		elif abs(val-num)<=2:
			print "%d almost perfect"%num
		else:
			print "%d not perfect"%num

main()
# stop = timeit.default_timer()

# print stop - start 
	