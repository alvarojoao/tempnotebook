#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("...........*........\n....*.....*.........\n.........*..*...*...\n*..*..*......***....\n..*.....*...........\n.*..................\n.......*.........*.*\n....................\n.....*............*.\n\n..........\n.*.**.*...\n*....*.*.*\n..........\n..*.....*.\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
        
    valueStars = []
    for line in sys.stdin:
        line = line.replace('\n','')
        if line == "":
            printResult(valueStars)
            valueStars = []
            print ""
            continue
        valueStars.append(line.count('*'))
    printResult(valueStars)

	# print counter(n)
def printResult(values):
    off = 0
    total  = sum(values)
    for val in values:
        line = "."*(total-val-off) + "*"*val + "."*off
        print line
        off += val



main()
# stop = timeit.default_timer()

# print stop - start 
	