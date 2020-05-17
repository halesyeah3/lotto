#!/bin/python3
from random import randint
import random

print('Welcome to the Lotto Game')

lottoNumbers = input('Enter your 5 lotto numbers (1-60) seperated by a comma')
#maybe int(lottoNumbers) after stripping commas from the list to validate numbers


#Need to add validation for the input from the user for the following
#Duplicate Numbers
#Non Numeric Values
#Numbers outside 1-60 range


lNumbers = lottoNumbers.split(",")
lNumber = [int(i) for i in lNumbers]

if all(i <= 60 for i in lNumber):
    print('Your Numbers:', lNumber)
#Clean this up
    lotto = random.sample(range(1, 60), 5)
    print('Winning Numbers: ', lotto)


#Count the number of matching numbers from user guess and lotto winners
    correctNum = sum(x == y for x, y in zip(lNumber, lotto))


        
#Notify the user of their result
    print('You got', correctNum, 'correct')

    if correctNum == 5:
        print('Congratulations! You won $100,000')
    elif correctNum == 4:
        print('Congratulations! You won $4,000')
    elif correctNum == 3:
        print('Congratulations! You won $5')
    else:
        print('Play Again')
        
else:
    lottoNumbers = input('Enter your 5 lotto numbers (1-60) seperated by a comma')
#Return to top instead?