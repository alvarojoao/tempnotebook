#! /usr/bin/python2

import sys
import math
import StringIO
import itertools
# import timeit


sys.stdin = StringIO.StringIO("2 10\n3 5 5\n5 2 2\n")
# sys.stdin = StringIO.StringIO("4 30\n7 13 5\n14 4 4\n15 3 10\n25 1 1\n")

# start = timeit.default_timer()


def main2():
    initial = 0
    N,L = map(int,sys.stdin.readline().replace('\n','').split(' '))
    lin = 0
    for line in xrange(N):
        D,R,G = map(int,sys.stdin.readline().replace('\n','').split(' '))
        initial += D-lin
        L -= D-lin
        lin = D
        tt = ((-1*(initial%(R+G)))+R)
        waitingTime = tt if tt>=0 else 0
        initial += waitingTime
        
        # print 'D,R,G',D,R,G
        # print 'waitingTime',waitingTime
        # print 'initial',initial
        # print 'L',L

        
        
    if L>0:
        initial += L
        L=0
    print initial

main2()
# stop = timeit.default_timer()

# print stop - start 
