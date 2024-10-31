actual_price = 10
guess_limit = 5
guess_count = 0

while guess_count < guess_limit:
  guess = int(input('Guess the price'))
  guess_count += 1
  if guess == actual_price:
    print('You won the game')
    break
else:
  print('You lost the game')
