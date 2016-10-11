#! /usr/bin/python2

import sys
import math
import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("10 3\n1 4 8\n")
sys.stdin = StringIO.StringIO("6 2\n2 5\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	width, numParts = map(int,sys.stdin.readline().replace('\n','').split(' '))
	parts = map(int,sys.stdin.readline().replace('\n','').split(' '))
	possible = [False]*(width+1)
	possible[width] = True;

	for i in  parts:
		possible[i] = True
		possible[width-i] = True
	
	for i in range(len(parts)):
		for j in range(i+1,len(parts)):
			possible[parts[j]-parts[i]]=True
	
	print " ".join([str(i)  for i,possi in enumerate(possible) if possi==True ])

	# for (int i = 0; i < numPartitions; i++) {
	# 	possible[partitions[i]] = true;
	# 	possible[width-partitions[i]] = true;
	# }
	# for (int i = 0; i < numPartitions; i++) {
	# 	for (int e = i+1; e < numPartitions; e++) {
	# 		possible[partitions[e] - partitions[i]] = true;
	# 	}
	# }
	# StringBuilder sb = new StringBuilder();
	# for (int i = 0; i < possible.length; i++) {
	# 	if (possible[i]) {
	# 		sb.append(i).append(" ");
	# 	}
	# }

main()
# stop = timeit.default_timer()

# print stop - start 
	