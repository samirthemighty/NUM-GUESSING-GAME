#Num guessing game
import random

print('Lets play a guessing number game!')
def guess_game():
  number = str(random.randint(1,9999))
  guess = ''
  attempts = 0
  while guess != number :
    attempts += 1
    guess = input('\nEnter a 4 digit number: ')
    list1 = []
    for i in number:
      list1.append(i)
    if len(guess) != 4:
      print('Must be 4 digits\n')
      continue
    current_positions = 0
    current_numbers = 0
    for i in range(len(number)):
      if guess[i] == number[i]:
        current_positions += 1
    for i in range(len(number)):
      if guess[i] in list1:
        list1.remove(guess[i])
        current_numbers += 1
    print(f'Current Numbers: {current_numbers}')
    print(f'Current Positions: {current_positions}\n')
  new_game = int(input(f'You guessed {number} correct in {attempts} guesses! Press 1 to try again or 2 to quit \n'))
  if new_game == 1:
    guess_game()
  else:
    return ' '
print(guess_game())
