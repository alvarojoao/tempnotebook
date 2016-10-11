#! /usr/bin/python2
from __future__ import division

import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("SECRET SOMECHEERSARETOUGH\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	line = sys.stdin.readline()
	string = line.replace('\n','')
	strings= string.split(" ")
	secret = strings[0].replace(' ','')
	message = strings[1].replace(' ','')
	secret = list(secret)

	for character in message:
		if len(secret)>0:
			if secret[0]==character:
				secret.pop(0)
			elif character in  secret[1:]:
				break
	
	if len(secret)<=0:
		print "PASS"
	else:
		print "FAIL"


main()
# stop = timeit.default_timer()

# print stop - start 
	