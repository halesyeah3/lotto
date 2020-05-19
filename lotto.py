  GNU nano 3.2                                            lotto.py                                                      
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
    lNumbers = lottoNumbers.split(",")
    try:
        lNumber = (int(i) for i in lNumbers)
        #Why does only one condition work?
        if all(i <= 60 for i in lNumber) and all(i >= 1 for i in lNumber):
            
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
        
    
