#! /usr/bin/python3

import sys
for line in sys.stdin: 
    posicao = 1
    for letter in line:
        if letter == "A":
            if posicao == 1:
                posicao = 2
            elif posicao == 2:
                posicao = 1
        elif letter == "B":
            if posicao ==2:
                posicao = 3
            elif posicao == 3:
                posicao = 2
        else:
            if posicao ==3:
                posicao = 1
            elif posicao == 1:
                posicao = 3
    break
print(posicao)
