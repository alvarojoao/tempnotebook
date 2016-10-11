#! /usr/bin/python2
import sys
import math
import StringIO
# import re
# import timeit

sys.stdin = StringIO.StringIO("apple\nbanana\ngrape\nkiwi\npear\n\napple\nbanana\ngrape\nkiwi\npear\n\napple\nbanana\ngrape\nkiwi\npear\n\napple\nbanana\ngrape\nkiwi\npear\n\nairplane\nbicycle\nboat\ncar\n")

# start = timeit.default_timer()
def main():
	words = []
	for line in sys.stdin:
		line = line.replace('\n','')
		if line == '':
			words.sort()
			maxIntString = max(map(lambda x:len(x),words))
			for w in words:
				print " "*(maxIntString-len(w))+w[::-1]
			words = []
		words.append(line[::-1])
	
	maxIntString = max(map(lambda x:len(x),words))
	words.sort()
	for w in words:
		print " "*(maxIntString-len(w))+w[::-1]
	# print "\n".join(map(lambda x:" "*(maxIntString-len(x))+x[::-1],words))
	# print "".join(map(lambda x:" "*(maxIntString-len(x))+x[::-1],words[-1:]))

main()
# stop = timeit.default_timer()

# print stop - start 
	