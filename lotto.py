#!/bin/python3
import random
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

#Do I need to make this a main function?  All the github labs said to do it this way.  What is the purpose?  Is it so I can just call main() in a try/except to restart the program?
def main():
  numString = input('Enter 5 Numbers (1-60) seperated by a comma: ')
  numList = numString.split(",")

  try:
    #The stupid list was returning empty for the second condition it took me a long time to figure out I had to add list() when converting the list to ints.  Not 100% sure why
    numbers = list(int(i) for i in numList)
    if (max(numbers) < 61 and min(numbers) > 0):
      print('Your Lotto Numbers:')
      print(numbers)
    
    #PLAN: Create a function that checks for dupe entries and add the if == True condition to the above if statement
      winningNum = random.sample(range(1, 60), 5)
      print('Winning Numbers:')
      print(winningNum)

      numCorrect = sum(x == y for x, y in zip(numList, winningNum))
      print('You got', numCorrect, 'correct')
      checkCorrect(numCorrect)

    else:
      #If I run in python3 CL this errors out with command not found
      print('nope')
  except:
    print('Bad Value - Enter numbers only')

if __name__== "__main__":
  main()
#Is this just saying this is the end of the function or something else?
