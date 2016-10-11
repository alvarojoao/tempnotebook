#! /usr/bin/python2

import sys
import math
import StringIO
# import timeit
t1 = "2^1^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2\n"
t2 = "100^10^1^10^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100^100\n"
t3 = "3^5 \n"
t4 = "100\n"
t5 = "20^10^21\n"


sys.stdin = StringIO.StringIO("5\n"+t1+t2+t3+t4+t5+"2\n"+t1+t3)
# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2

# start = timeit.default_timer()

minVALUE = -sys.maxsize - 1

def logN(val , rep):
	valFinal = val
	for i in range(rep):
		valFinal = (minVALUE) if (valFinal)<=0 else math.log(valFinal)
	return valFinal

def treatOnes(stringExp):
	isOne= False
	newString = []
	for number in stringExp.split("^"):
		if int(number)==1:
			isOne = True
			newString.append(number)
		if(not isOne):
			newString.append(number)
	return "^".join(newString)


def letter_cmp(a, b):
	a = treatOnes(a)
	b = treatOnes(b)
	numLog = max([a.count("^"),b.count("^")])
	a = a+"^1"*(numLog-a.count("^"))
	b = b+"^1"*(numLog-b.count("^"))
	a = map(int,a.split("^"))
	b = map(int,b.split("^"))
	aVal = 0
	bVal = 0
	for i in range(numLog):

		finalA = a[i+1]if len(a)-2==i else 1
		finalB = b[i+1]if len(b)-2==i else 1
		aVal += (logN(a[i],numLog-i))*(finalA)
		bVal += (logN(b[i],numLog-i))*(finalB)

	if aVal >= bVal:
		return 1
	else:
		return -1

def letter_cmp2(a, b):
	a = treatOnes(a)
	b = treatOnes(b)
	numLog = max([a.count("^"),b.count("^")])
	a = a+"^1"*(numLog-a.count("^"))
	b = b+"^1"*(numLog-b.count("^"))
	a = map(int,a.split("^"))
	b = map(int,b.split("^"))
	aVal = 1
	bVal = 1
	for i in range(numLog+1)[::-1]:
		aVal *= (a[i] if 0!=i else  math.log(a[i]))
		bVal *= (b[i] if 0!=i else  math.log(b[i]))
	print aVal
	print bVal
	if aVal >= bVal:
		return 1
	else:
		return -1

print letter_cmp2("3^4", "100")

def main():
	count = 0
	for line in sys.stdin:
		num = int(line)
		order = []
		for num2 in range(num):
			stringPow = sys.stdin.readline()
			stringPow = stringPow.strip().replace("\n","")
			order.append(stringPow)

		order.sort(letter_cmp2)
		count += 1
		if count>1:
			print ""
		print 'Case {0:1d}:'.format(count)
		print "\n".join([aa for aa in order])

# main()
# stop = timeit.default_timer()

# print stop - start 
	