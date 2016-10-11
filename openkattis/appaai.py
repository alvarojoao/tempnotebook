#! /usr/bin/python2

import sys

anterior = ""
newName = ""
for line in sys.stdin:
	for letter in line:
		if(anterior!=letter):
			newName+=letter
			anterior = letter
	print newName
