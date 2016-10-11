#! /usr/bin/python2
from __future__ import division

import sys
import math
from collections import Counter
import StringIO
# import re
# import timeit

# sys.stdin = StringIO.StringIO("1 4 1 4\n1 6 1 6\n")#3^4\n15\n9^2
# sys.stdin = StringIO.StringIO("1 8 1 8\n1 10 2 5\n")#3^4\n15\n9^2
# sys.stdin = StringIO.StringIO("2 5 2 7\n1 5 2 5\n")#3^4\n15\n9^2

# start = timeit.default_timer()


def main():

	gunnarString = sys.stdin.readline().replace('\n','').split(' ')
	emmaString = sys.stdin.readline().replace('\n','').split(' ')

	gunnar1a = int(gunnarString[0])
	gunnar1b = int(gunnarString[1])

	gunnar2a = int(gunnarString[2])
	gunnar2b = int(gunnarString[3])

	emma1a = int(emmaString[0])
	emma1b = int(emmaString[1])

	emma2a = int(emmaString[2])
	emma2b = int(emmaString[3])


	gunner = (gunnar1a+gunnar1b)/2 + (gunnar2a+gunnar2b)/2 
	emma = (emma1a+emma1b)/2 + (emma2a+emma2b)/2 
	
	if :

	# possiveisGunner = list(set([i+j for i in range(gunnar1a,gunnar1b+1) for j in range(gunnar2a,gunnar2b+1)]))
	# changesGunner = [(p,i,j) for p in possiveisGunner for i in range(gunnar1a,gunnar1b+1) for j in range(gunnar2a,gunnar2b+1) if (i+j)==p  ]
	# totalChangesGunner = len(changesGunner) 
	# mpGunner  = map(lambda (x,y,z): x,changesGunner)
	# finalGunner = mpGunner#Counter(mpGunner)

	# possiveisEmma = list(set([i+j for i in range(emma1a,emma1b+1) for j in range(emma2a,emma2b+1)]))
	# changesEmma = [(p,i,j) for p in possiveisEmma for i in range(emma1a,emma1b+1) for j in range(emma2a,emma2b+1) if (i+j)==p  ]
	# totalChangesEmma = len(changesEmma) 
	# mpEmma  = map(lambda (x,y,z): x,changesEmma)
	# finalEmma = mpEmma#Counter(mpEmma)

	# # gunnerWinEmma = [ (i,finalGunner[i]) for i in finalGunner for j in finalEmma if i>j]
	# # emmaWinGunner = [ (i,finalEmma[i]) for i in finalEmma for j in finalGunner if i>j]
	# gunnerWinEmma = [ i for i in finalGunner for j in finalEmma if i>j]
	# emmaWinGunner = [ i for i in finalEmma for j in finalGunner if i>j]
	# if len(gunnerWinEmma)>len(emmaWinGunner):
	# 	print 'Gunnar'
	# elif len(gunnerWinEmma)<len(emmaWinGunner):
	# 	print 'Emma'
	# else:
	# 	print 'Tie'

main()
# stop = timeit.default_timer()

# print stop - start 
	