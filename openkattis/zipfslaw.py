#! /usr/bin/python2
import sys
import math
import StringIO
import re
import timeit

# sys.stdin = StringIO.StringIO("2\n\nIn practice, the difference between theory and practice is always\ngreater than the difference between theory and practice in theory.\n        - Anonymous\n\nMan will occasionally stumble over the truth, but most of the\ntime he will pick himself up and continue on.\n        - W. S. L. Churchill\nEndOfText\n2\n\nIn practice, the difference between theory and practice is always\ngreater than the difference between theory and practice in theory.\n        - Anonymous\n\nMan will occasionally stumble over the truth, but most of the\ntime he will pick himself up and continue on.\n        - W. S. L. Churchill\nEndOfText\n")#3^4\n15\n9^2
# start = timeit.default_timer()
def main():
    while(True):
        words = dict()
        try:
            n = int(sys.stdin.readline().replace('\n',''))
        except:
            break
        for line in sys.stdin:
            line = line.replace('\n','').lower()
            if line == 'endoftext':
                break
            for w in re.findall('\w\w+',line):
                words[w] = words.get(w,0)+1
        filtered = filter( lambda (x,y): y==n ,words.items())
        if len(filtered) == 0:
            print 'There is no such word.'
        else:
            print "\n".join(sorted(map(lambda x:x[0],filtered)))
        print ""

main()
# stop = timeit.default_timer()

# print stop - start 
	