#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("dog ogday\ncat atcay\npig igpay\nfroot ootfray\nloops oopslay\n\natcay\nittenkay\noopslay\n")

# start = timeit.default_timer()
def main():
	dictionary = {}
	for line in sys.stdin:
		if line.replace('\n','')=='':
			break
		value,key = line.replace('\n','').split(' ')
		dictionary[key] = value


	for line in sys.stdin:
		key = line.replace('\n','')
		if dictionary.has_key(key):
			print dictionary[key]
		else:
			print "eh"



main()
# stop = timeit.default_timer()

# print stop - start 
	