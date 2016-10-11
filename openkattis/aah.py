#! /usr/bin/python2

import sys

for line in sys.stdin:
	for line2 in sys.stdin: 
		print 'go' if len(line)>=len(line2) else 'no'