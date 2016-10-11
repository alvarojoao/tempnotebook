#! /usr/bin/python2

import sys
import StringIO

# import timeit
sys.stdin = StringIO.StringIO("3\n7\nsaskatoon\ntoronto\nwinnipeg\ntoronto\nvancouver\nsaskatoon\ntoronto\n4\na\na\na\na\n2")

num = int(sys.stdin.readline())
for num2 in range(num):
	numCity = int(sys.stdin.readline())
	city = []
	for num2 in range(numCity):
		nome = sys.stdin.readline()
		nome = nome.strip().upper()
		if not nome in city:
			city.append(nome)
	print len(city)

# stop = timeit.default_timer()

# print stop - start 
