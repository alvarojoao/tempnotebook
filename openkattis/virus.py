#! /usr/bin/python2

import sys
import math
import StringIO
# import re
# import timeit


sys.stdin = StringIO.StringIO("AAAAA\nAGCGAA\n")
# sys.stdin = StringIO.StringIO("GTTTGACACACATT\nGTTTGACCACAT\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	# original = map(lambda x:x,sys.stdin.readline().replace('\n',''))
	# alter = map(lambda x:x,sys.stdin.readline().replace('\n',''))
	
	original = sys.stdin.readline().replace('\n','')
	alter = sys.stdin.readline().replace('\n','')
	if len(alter)>len(original):
		for index,chart in enumerate(original):
			if index >= len(alter):
				break
			if alter[index] == chart:
				alter = alter[:index] + " " + alter[index + 1:]
		filtered = filter(lambda x: not x=='', alter.split(' '))
		filteredI = filter(lambda x: x not in original,filtered)
	print filteredI
	print filtered
	print alter


def substract(a, b):                              
    return "".join(a.rsplit(b))

main()
# stop = timeit.default_timer()

# print stop - start 
	