#! /usr/bin/python2

import sys
import math
# import StringIO
import itertools
# import timeit


# sys.stdin = StringIO.StringIO("20\n40 50 60 70 120 130 140 180 190 200 1 2 3 4 5 10 11 12 13 14\n")
# sys.stdin = StringIO.StringIO("100 100 1 1 1\n200 100 5 3 4\n201 132 48 1900 156\n0 0 0 0 0\n")
# sys.stdin = StringIO.StringIO("40\n1 2 3 4 5 10 11 12 13 14 15 16 20 21 22 23 24 30 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 60 70 120\n")

# start = timeit.default_timer()

def main2():
	for line in sys.stdin:
		line = line.replace('\n','')
		if line.count('0')>=5:
			break
		width ,height  ,s,numVertBounces ,numHorizBounces  = map(float,line.split(' '))
		angle = math.degrees(math.atan2(height*numHorizBounces, width*numVertBounces));
		velocity = math.sqrt(((height*numHorizBounces)**2) + ((width*numVertBounces)**2))/s;
		print "%.2f %.2f" % (angle,velocity)


main2()
# stop = timeit.default_timer()

# print stop - start 