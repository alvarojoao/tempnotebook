#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("6\n180 181 182 141 174 143 142 175\n")
# sys.stdin = StringIO.StringIO("3\n4 4 4\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	values = map(int,sys.stdin.readline().replace('\n','').split(' '))
	values.sort(key=int)
	stringList = []
	first = None
	i = 0
	while i<len(values):
		first = values[i]
		string = str(first)
		j = i
		lastN = None
		count =0
		while(j<len(values)-1):
			if values[j]+1 == values[j+1]:
				count+=1
				if count>1:
					lastN = values[j+1]
				j+=1
			else:
				break
		if count>1:
			i = j
		i+=1
		string = string + ("" if lastN == None else "-"+str(lastN))
		stringList.append(string)

	print " ".join(stringList)


main()
# stop = timeit.default_timer()

# print stop - start 
	