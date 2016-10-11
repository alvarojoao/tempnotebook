#! /usr/bin/python2
import sys
import math
import StringIO
import re
import timeit

sys.stdin = StringIO.StringIO("5 3\n.*S#.\n.....\n....#\n.*...\n.S...\n")
# start = timeit.default_timer()
def main():
    N,R = map(int,sys.stdin.readline().replace('\n','').split(' '))
    
    print N,R

main()
# stop = timeit.default_timer()

# print stop - start 
	