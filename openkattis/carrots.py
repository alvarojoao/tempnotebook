#! /usr/bin/python3

import sys

#num = sys.stdin
first = false
for line in sys.stdin:
    if first:
        num = int(line);
    else:
        string = "is odd" if number%2==0 else"is even"
        print(number+string)

