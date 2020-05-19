#!/bin/python3

from random import randint
import random

def checkRange(num):
#Check the Range of a value
    if num in range(1,60):
        print('valid range')
        print(num)
    else:
        print ('invalid range')

def checkDupe(listOfElems):
#Check if given list contains any duplicates
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

#Take in User Input
lottoString = input('Enter your 5 lotto numbers (1-60) seperated by a comma')

#Convert Input to List
lNumbers = lottoString.split(",")

#Validate Input for integers
try:
    lNumber = (int(i) for i in lNumbers)
except ValueError:
    print('Not a Number')
    #Restart the loop back to User Input
    
#value range
try:
    for eachItem in lNumber:
        checkRange(eachItem)
except ValueError:
    print(ValueError)
    
#duplicates
try:
    for eachItem in lNumber:
        count =  checkDupe(lNumber)
        if count:
            print('Duplicate Entry')
        else:
            print('Not a Dupe')

except ValueError:
    print('Duplicate Entry')

#If invalid send back to User Input, If valid continue

#Generate winning Lotto Numbers

#Compare User Input to Winning Lotto Numbers

#Print Result

#Play Again? Feature that loops to beginning



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


'''
while True:

    
    lottoNumbers = input('Enter your 5 lotto numbers (1-60) seperated by a comma')
    lNumbers = lottoNumbers.split(",")
    try:
        def checkRange(num):
            if (1 <= num <= 60):
                print('range valid')
                print(num)
                return True
            else:
                return False
            
        lNumber = (int(i) for i in lNumbers)
        #Why does only one condition work?
        #I want to check the range between 1-60 & check for duplicates
        for eachItem in lNumber:
            checkRange(eachItem)
            
           
#Should only draw lotto numbers if validation is met
            lotto = random.sample(range(1, 60), 5)
            print('Your Numbers: ', lNumbers)
            print('Winning Numbers: ', lotto)
        #Count the number of matching numbers from user guess and lotto winners
            correctNum = sum(x == y for x, y in zip(lNumber, lotto))
            print('You got', correctNum, 'correct')

            if correctNum == 5:
                print('Congratulations! You won $100,000')
            elif correctNum == 4:
                print('Congratulations! You won $4,000')
            elif correctNum == 3:
                print('Congratulations! You won $5')
            else:
                print('Thanks for Playing!')
            #Loop Back after input from user
            #playagain = input('Play Again? Y/N')
            #if playagain == 'Y' or playagain == 'y':
            #    continue
            #else:
            #    print('Thanks For Playing!')
    
        else:
            continue
    except ValueError:
        continue
'''        
    
