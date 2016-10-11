#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("5 3 8\n")

# start = timeit.default_timer()
def main():
	x,y,result = map(int,sys.stdin.readline().replace('\n','').split(' '))
	if x+y == result:
		print "%d+%d=%d"%(x,y,result)
	elif x-y == result:
		print "%d-%d=%d"%(x,y,result)
	elif x*y == result:
		print "%d*%d=%d"%(x,y,result)
	elif x/y == result:
		print "%d/%d=%d"%(x,y,result)
	elif x==y + result:
		print "%d=%d+%d"%(x,y,result)
	elif x==y - result:
		print "%d=%d-%d"%(x,y,result)
	elif x==y * result:
		print "%d=%d*%d"%(x,y,result)
	elif x==y / result:
		print "%d=%d/%d"%(x,y,result)

main()
# stop = timeit.default_timer()

# print stop - start 
	