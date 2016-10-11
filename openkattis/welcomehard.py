#! /usr/bin/python2

import sys
import math
import StringIO
# import re
# import timeit
import itertools

# sys.stdin = StringIO.StringIO("dcbagfekjih\nmobitel\nanakonda\n")
# sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\n")
sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\nwweellccoommee to code qps jam\nwelcome to codejam\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
welcomeStr = "welcome to code jam"
def main():
	n = int(sys.stdin.readline().replace('\n','').replace(' ',''))
	for i in range(n):
		line = sys.stdin.readline().replace('\n','')

		for i,char in enumerate(line):
			for j in range(i,len(line)):
				
main()
# stop = timeit.default_timer()

# print stop - start 
		