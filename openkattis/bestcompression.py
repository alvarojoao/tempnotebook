#! /usr/bin/python2

import sys
import math
# import StringIO
import re
# import timeit


# sys.stdin = StringIO.StringIO("13 3\n1 0\n31415926535897 40\n")
# sys.stdin = StringIO.StringIO("1 0\n31415926535897 40\n")
# sys.stdin = StringIO.StringIO("31415926535897 40\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	num1,num2 = map(int,sys.stdin.readline().replace("\n","").split(" "))
	num = math.pow(2, num2+1)-1
	print "yes" if num1 <= num else "no"
main()
# stop = timeit.default_timer()

# print stop - start 
	