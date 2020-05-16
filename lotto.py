#!/bin/python3
from random import randint

print('Welcome to the Lotto Game')

lottoNumbers = input('Enter your 5 lotto numbers (1-60) seperated by a comma')
#maybe int(lottoNumbers) after stripping commas from the list to validate numbers


#Need to add validation for the input from the user for the following
#Duplicate Numbers
#Non Numeric Values
#Numbers outside 1-60 range


lNumbers = lottoNumbers.split(",")
lNumber = [int(i) for i in lNumbers]

print('Your Numbers:', lNumber)

#There has to be a better way to generate 5 random numbers with the same min/max
#Currently these numbers can duplicate but should be unique
num1 = randint(1,60) #1
num2 = randint(1,60) #2
num3 = randint(1,60) #3
num4 = randint(1,60) #4
num5 = randint(1,60) #5

#Clean this up
lotto = [num1, num2, num3, num4, num5]
lottoWinners = str(lotto)
print('Winning Numbers: ', lottoWinners)


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