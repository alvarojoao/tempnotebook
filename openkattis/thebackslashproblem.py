#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("1\nthis is a 'test'\n2\n/:-)\n")
# sys.stdin = StringIO.StringIO("100 5\n42\n3\n2\n99\n1\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	for line in sys.stdin:
		n = int(line.replace('\n',''))
		stringV = sys.stdin.readline().replace('\n','')
		returnV = ""
		for chart in stringV:
			if (ord(chart) >= ord('!') and ord(chart) <= ord('*') )or (ord(chart) >= ord('[') and ord(chart) <= ord(']') ):
				i = 2**(n)
				while i >1:
					i -=1
					returnV += "\\"
			returnV +=chart
		print returnV



main()
# stop = timeit.default_timer()

# print stop - start 
	