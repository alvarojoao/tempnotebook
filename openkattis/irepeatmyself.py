#! /usr/bin/python2
from __future__ import division

import sys
import math
import StringIO
# import itertools
# import timeit


# sys.stdin = StringIO.StringIO("4\n \nI Repeat Myself I Repeat Myself I Repeat\naaaaaaaaaaaaaaaaaaaaa\nabbcabbcabbabbcabb\n")
sys.stdin = StringIO.StringIO("1\nabc abc abc a\n")

# start = timeit.default_timer()

# def main():
# 	num = int(sys.stdin.readline().replace('\n',''))
# 	for s in range(num):
# 		line = sys.stdin.readline().replace('\n','')
# 		for i in range(1,len(line)+1):
# 			subString =  line[:i]
# 			div = int(math.ceil(len(line)/i))
# 			builder = ""
# 			for j in range(div):
# 				builder+=subString
# 			if builder.startswith(line):
# 				print i
# 				break
def main():
	num = int(sys.stdin.readline().replace('\n',''))
	for s in range(num):
		settence = sys.stdin.readline().replace('\n','')
		for subIndex in range(1,len(settence)+1):
			subSequence = settence[:subIndex]
			div = int(math.ceil(len(settence)/subIndex))
			builder = ""
			for j in range(div):
				builder+=subSequence
			if builder[:len(settence)]==settence:
				print subIndex
				break
			
main()
# stop = timeit.default_timer()

# print stop - start 