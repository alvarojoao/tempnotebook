#! /usr/bin/python2

import sys
import math
# import StringIO
# import timeit


# sys.stdin = StringIO.StringIO("1000000\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2

# start = timeit.default_timer()

# def main():
# 	for line in sys.stdin:
# 		num = int(line)
# 		orderMax = []
# 		for numT in range(1,10)[::-1]:
# 			order = [numT]
# 			for num2 in range(1,numT)[::-1]:
# 				if order[-1]% num2 == 0:
# 					order.append(num2)
# 			if len(order)>len(orderMax):
# 				order.sort(key=int,reverse=False)
# 				orderMax = order
# 		print len(orderMax)
#         print " ".join(map(str,orderMax))
def main2():
	for line in sys.stdin:
		num = int(line)
		orderMax = []
		for numT in range(2,8):
			order = [1]
			filter(lambda x:testcase(x,order),range(numT,num+1))
			if len(order)>=len(orderMax):
				orderMax = order
		print len(orderMax)
        print " ".join(map(str,orderMax))

def testcase(value,order):
	if value%order[-1] == 0:
		order.append(value)
	return value%order[-1] == 0
main2()
# stop = timeit.default_timer()

# print stop - start 