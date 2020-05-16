#!/bin/python3
from random import randint

print('Welcome to the Lotto Game')

lottoNumbers = input('Enter your 5 lotto numbers (1-60) seperated by a comma')

#Need to add validation for the input from the user - unique numbers only and 1-60


lNumbers = lottoNumbers.split(",")
lNumber = [int(i) for i in lNumbers]

print(lNumber)

#There has to be a better way to generate 5 random numbers with the same min/max
num1 = randint(1,60)
num2 = randint(1,60)
num3 = randint(1,60)
num4 = randint(1,60)
num5 = randint(1,60)

lotto = [num1, num2, num3, num4, num5]
lottoWinners = str(lotto)
print(lottoWinners)


#Count the number of matching numbers from user guess and lotto winners
correctNum = sum(x == y for x, y in zip(lNumber, lotto))


        
#Notify the user of their result
print('You got', correctNum, 'correct')
