#! /usr/bin/python2

import sys
import math
import StringIO
# import re
# import timeit
import itertools

# sys.stdin = StringIO.StringIO("dcbagfekjih\nmobitel\nanakonda\n")
# sys.stdin = StringIO.StringIO("1\nelcomew elcome to code jam\n")
sys.stdin = StringIO.StringIO("3\nelcomew elcome to code jam\nwweellccoommee to code qps jam\nwelcome to codejam\n")
# sys.stdin = StringIO.StringIO("a\n.\n")
# start = timeit.default_timer()
welcomeStr = "welcome to code jam"
def main():
	n = int(sys.stdin.readline().replace('\n','').replace(' ',''))
	for i in range(n):
		line = sys.stdin.readline().replace('\n','')
		dp = [0 for j in range(len(line))[for w in range(len(welcomeStr))]]
		for l,letter in enumerate(welcomeStr)[::-1]:
			sum = 0
			for k in range(len(line)-1-len(welcomeStr)-1-l):
				if line[k]==welcomeStr[l]:
					if l==len(welcomeStr)-1:
						sum+=1
					else:
						sum+=dp[l+1][k+1]
					sum %= 10000
					dp[l][k] = sum
		print "Case #%d: %04d"%(i+1, dp[0][0])
				
main()
# stop = timeit.default_timer()

# print stop - start 
		