import random
def rollDice(dice):
    n = random.random()
    sum_ = 0
    for i,dice_ in enumerate(dice):
        if sum_<n and n<= dice_+sum_ :
            return i+1
        sum_ +=dice_

dice = [0.32,0.32,0.12,0.04,0.07,0.13]
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
print rollDice(dice)
