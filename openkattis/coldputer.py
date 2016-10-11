#! /usr/bin/python3

import sys


for line in sys.stdin: 
    days = int(line)
    for day in sys.stdin:
        temps = map(int,day.split())
        print(sum(1 for temp in temps if temp < 0))
        break
