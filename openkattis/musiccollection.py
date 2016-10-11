#! /usr/bin/python2

import sys
import math
# import StringIO
# import re
# import timeit


# sys.stdin = StringIO.StringIO("5\n6\nA Perfect Circle - Gravity\nAimee Mann - You Do\nAqualung - Cinderella\nArcade Fire - Haiti\nArt of Noise - Pleure\nATB - Marrakech\n2\nHybrid - Altitude\nKings of Convenience - The Build-up\n3\naaaaaaaabb\naaaaaaabbb\nababababab\n3\nbutter\nfly\nbutterfly\n1\nUnknown Artist - Track On\n")
# sys.stdin = StringIO.StringIO("1\n6\nA Perfect Circle - Gravity\nAimee Mann - You Do\nAqualung - Cinderella\nArcade Fire - Haiti\nArt of Noise - Pleure\nATB - Marrakech\n")
# sys.stdin = StringIO.StringIO("100 5\n42\n3\n2\n99\n1\n")

# sys.stdin = StringIO.StringIO("4\n2^2^2\n3^4\n15\n9^2")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
	n = int(sys.stdin.readline().replace('\n',''))
	for i in range(1,n+1):
		p = int(sys.stdin.readline().replace('\n',''))
		playList = []
		for j in range(p):
			playList.append(sys.stdin.readline().replace('\n','').upper())

		minStringAndSong = []
		if len(playList)==1:
			minStringAndSong.append("\"\"")
		else:
			for num,song in enumerate(playList):
				minStringAndSong.append(getMinString(num,song,playList))

		print "Case #%d:"%(i)
		print "\n".join(minStringAndSong)


def getMinString(i,song,playList):
	minStringAndSong = ""
	founded = False
	for tan in range(1,len(song)+1):
		for step in range(len(song)-tan+1):
			subString = song[step:tan+step]
			checked = checkSubInList(subString,playList)
			if len(checked)== 1 and checked[0]==i:
				founded = True
				if minStringAndSong == "":
					minStringAndSong = subString
				else:
					minStringAndSong = subString if subString<minStringAndSong else minStringAndSong
		if founded:
			break
	if minStringAndSong !="":
		return "\"%s\"" % minStringAndSong
	else:
		return ":("

def checkSubInList(subString,playList):
	return [i for i,song in enumerate(playList) if subString in song]

main()
# stop = timeit.default_timer()

# print stop - start 
	