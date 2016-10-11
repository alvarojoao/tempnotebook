#! /usr/bin/python2
import sys
import math
# import StringIO
# import re
# import timeit
# sys.stdin = StringIO.StringIO("1\n5\nmom: upper-upper-lower-middle class\ndad: middle-middle-middle-lower-middle class\nqueenelizabeth: upper-upper-upper class\nchair: lower-lower class\nunclebob: middle-middle-lower-middle class\n")

# sys.stdin = StringIO.StringIO("1\n6\nZom: upper-upper-lower-middle class\nmom: upper-upper-lower-middle class\ndad: middle-middle-middle-lower-middle class\nqueenelizabeth: upper-upper-upper class\nchair: lower-lower class\nunclebob: middle-middle-lower-middle class\n")
# sys.stdin = StringIO.StringIO("1\n2\nZom: upper-upper-lower-middle class\nmom: upper-upper-lower-middle class\n")

# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for inst in range(n):
		numPessoas = int(sys.stdin.readline().replace('\n',''))
		pessoas = []
		for i in range(numPessoas):
			pessoa,classe = map(str,sys.stdin.readline().replace('\n','').split(':'))
			classe = classe.replace("class", "").strip().replace("upper", "0").replace("middle", "1").replace("lower", "2").replace("-", "")[::-1]
			classe+="1111111111"
			pessoas.append((pessoa,classe))
		pessoas.sort(cmp=comparePerson)
		print "\n".join(map(lambda x:x[0],pessoas))
		print "=============================="

def comparePerson(a,b):
	i = 0
	while i<len(a[1]) and i<len(b[1]):
		if a[1][i] != b[1][i]:
			return ord(a[1][i]) - ord(b[1][i])
		i+=1
	if a[0]>b[0]:
		return 1
	else:
		return -1



main()
# stop = timeit.default_timer()

# print stop - start 
	