#! /usr/bin/python3

import sys

num = int(raw_input())

for i in range(num): 
    number = int(raw_input())
    string = " is even" if number%2==0 else" is odd"
    print(str(number)+string)
