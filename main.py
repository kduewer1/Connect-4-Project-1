guesslist = [1, 2, 7, 4, 25, 15, 12, 21, 16, 9]
score = 0
print("Welcome to the guessing game! To play, guess a number between 1 and 25. Guess all ten numbers correctly to win!")
print("Also, don't guess the same number multiple times.")
while score < 10:
  try:
    ask = int(input("What is your guess?: " ))
  except ValueError:
    print("Boi you gotta enter a number. Try again!")
    continue
  #if ask == guesslist[0] or ask == guesslist[1] or ask == guesslist[2] or ask == guesslist[3] or ask == guesslist[4] or ask == guesslist[5] or ask == guesslist[6] or ask == guesslist[7] or ask == guesslist[8] or ask == guesslist[9]:
  guesslist = set(guesslist)
  if ask in guesslist:
    print("You guessed correctly! You got a point!")
    print("The number was " + str(ask))
    score = score + 1
    print("Score: " + str(score))
  elif ask > 25:
    print("That number is too high! Try again!")
  elif ask < 1:
    print("That number is too low! Try agian!")
  else:
    print("Incorrect guess. Try again!")

print("Congrats! You won!")