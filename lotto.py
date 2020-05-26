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

def main():
  numString = input('Enter 5 Numbers (1-60) seperated by a comma: ')
  numList = numString.split(",")

  try:
    numbers = list(int(i) for i in numList)
    if (max(numbers) < 61 and min(numbers) > 0):
      print('Your Lotto Numbers:')
      print(numbers)

      winningNum = random.sample(range(1, 60), 5)
      print('Winning Numbers:')
      print(winningNum)

      numCorrect = sum(x == y for x, y in zip(numList, winningNum))
      print('You got', numCorrect, 'correct')
      checkCorrect(numCorrect)

    else:
      print('nope')
  except:
    print('Bad Value - Enter numbers only')

if __name__== "__main__":
  main()
