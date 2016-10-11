#! /usr/bin/python2

import sys
import math
import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("16")

# sys.stdin = StringIO.StringIO("OPEN\nENTER Sam 0\nENTER Alice 15\nEXIT Sam 20\nEXIT Alice 700\nCLOSE\nOPEN\nENTER Sam 5\nENTER Alice 10\nEXIT Sam 20\nEXIT Alice 35\nENTER Sam 700\nEXIT Sam 710\nCLOSE")#3^4\n15\n9^2
# start = timeit.default_timer()
OPEN = 'OPEN'
ENTER = 'ENTER' 
EXIT = 'EXIT' 
CLOSE = 'CLOSE'
FINAL = 'FINAL'
price = 0.10
def main():
	day = 1
	for line in sys.stdin:
		line = line.replace('\n','')
		if line == OPEN:
			mapUser = dict()
			mapUserList = {}
			for lineWhile in sys.stdin:
				lineWhile = lineWhile.replace('\n','')
				if lineWhile == CLOSE:
					break
				status,name,value = lineWhile.split(' ')
				if status == ENTER:
					mapUser[name] = mapUser.get(name,{})
					mapUser[name][status] = int(value)
				else:
					mapUser[name][status]=int(value)
					difference = mapUser[name][EXIT]-mapUser[name][ENTER]
					mapUser[name][FINAL]=(mapUser[name].get(FINAL,0)+difference*price)
					mapUserList[name] = "$%.2f"%(mapUser[name][FINAL])
			mapUserList = mapUserList.items()
			mapUserList.sort(key=lambda x:x[0],reverse=False)
			print "Day %d"%(day)
			print "\n".join(map(lambda (x,y):x+' '+y,mapUserList))
			print ""
			day+=1


main()
# stop = timeit.default_timer()

# print stop - start 
	