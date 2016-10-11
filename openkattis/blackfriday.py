#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("8\n1 1 1 5 3 4 6 6\n")
# sys.stdin = StringIO.StringIO("3\n4 4 4\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	indexes = range(1,n)
	values = map(int,sys.stdin.readline().replace('\n','').split(' '))
	dictionary = {}
	for i,value in enumerate(values):
		if dictionary.has_key(value):
			dictionary[value]['value'] +=1 
		else:
			dictionary[value] = {'index':(i+1),'value':1}
	filtered = filter(lambda (x,v):v['value']==1,dictionary.iteritems())
	if len(filtered)>0:
		print (max(filtered,key=lambda (x,v):x))[1]['index']
	else:
		print "none"


main()
# stop = timeit.default_timer()

# print stop - start 
	