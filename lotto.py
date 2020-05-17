#!/bin/python3
from random import randint
import random

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
    
def checkCorrect(int):
    if int == 5:
        print('Congratulations! You won $100,000')    
    elif int == 4:
        print('Congratulations! You won $4,000')    
    elif int == 3:
        print('Congratulations! You won $5')    
    else:
        print('Play Again')   
        print('Welcome to the Lotto Game')
        
while True:
    lottoNumbers = input('Enter your 5 lotto numbers (1-60) seperated by a comma')
#maybe int(lottoNumbers) after stripping commas from the list to validate numbers
    lNumbers = lottoNumbers.split(",")
#This isn't working
    try:
        lNumber = [int(i) for i in lNumbers]
        if all(i > 60 for i in lNumber) or all(i < 0 for i in lNumber):
            continue
        else:
            result = checkIfDuplicates_1(lNumbers)

        
        if result:
            continue
        else:
#Clean this up
                lotto = 1, 2, 3, 4, 5 #random.sample(range(1, 60), 5)
                print('Winning Numbers: ', lotto)

#Count the number of matching numbers from user guess and lotto winners
                
        
#Notify the user of their result
                correctNum = sum(x == y for x, y in zip(lNumber, lotto))
                print('Your Numbers:', lNumber)
                print('You got', correctNum, 'correct')
                checkCorrect(correctNum)
#Determine if Winner
    except ValueError:
        continue

    

            
        
        
#lottoNumbers = input('Enter your 5 lotto numbers (1-60) seperated by a comma')
#Return to top instead?