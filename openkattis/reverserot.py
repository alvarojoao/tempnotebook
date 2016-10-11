#! /usr/bin/python2

import sys
import math
import StringIO
import re
# import timeit


sys.stdin = StringIO.StringIO("1 ABCDEFGHIJKLMNOPQRSTUVWXYZ_.\n3 YO_THERE.\n1 .DOT\n14 ROAD\n9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING\n2 STRING_TO_BE_CONVERTED\n1 SNQZDRQDUDQ\n1 ABCDEFGHIJKLMNOPQRSTUVWXYZ_.\n3 YO_THERE.\n1 .DOT\n14 ROAD\n9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING\n2 STRING_TO_BE_CONVERTED\n1 SNQZDRQDUDQ\n1 ABCDEFGHIJKLMNOPQRSTUVWXYZ_.\n3 YO_THERE.\n1 .DOT\n14 ROAD\n9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING\n2 STRING_TO_BE_CONVERTED\n1 SNQZDRQDUDQ\n1 ABCDEFGHIJKLMNOPQRSTUVWXYZ_.\n3 YO_THERE.\n1 .DOT\n14 ROAD\n9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING\n2 STRING_TO_BE_CONVERTED\n1 SNQZDRQDUDQ\n1 ABCDEFGHIJKLMNOPQRSTUVWXYZ_.\n3 YO_THERE.\n1 .DOT\n14 ROAD\n9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING\n2 STRING_TO_BE_CONVERTED\n1 SNQZDRQDUDQ\n0\n")
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
finalString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def main():
	for line in sys.stdin:
		lines = line.split(" ")
		if int(lines[0])==0:
			break
		
		num = int(lines[0])
		string = lines[1].replace("\n","")
		newString = ""
		for character in string:
			newString+=finalString[(finalString.find(character.upper())+num)%len(finalString)]
		print newString[::-1]
main()
# stop = timeit.default_timer()

# print stop - start 
	