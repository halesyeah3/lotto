#!/bin/python3
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

#Take in User Input
while True:
  lottoString = input('Enter your 5 lotto numbers (1-60) seperated by a comma')

#Convert Input to List
  lNumbers = lottoString.split(",")

#Validate Input for integers
  try:
    lNumber = (int(i) for i in lNumbers)
    if ((checkRange(lNumber) == False and checkDupe(lNumber) == True) for i in lNumber):
      lotto = random.sample(range(1, 60), 5)
      print('Your Numbers: ', lNumbers)
      print('Winning Numbers: ', lotto)
        #Count the number of matching numbers from user guess and lotto winners
      correctNum = sum(x == y for x, y in zip(lNumber, lotto))
      print('You got', correctNum, 'correct')
      checkCorrect(correctNum)
    else:
      raise Exception("Not a valid input")



  except ValueError:
    print('Bad Value')
    continue
    #if ((lNumber < 0 or lNumber > 60 or lNumber is not int) for i in lNumber):

