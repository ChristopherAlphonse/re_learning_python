import random

roll = str(random.randint(1, 6))
user_guess_input = input("Guess the number rolled on the dice: \n")


if (user_guess_input == roll):
    print("You guessed correctly! The number rolled was " + roll)
else:
    print("Wrong")
