import random
computer_choice= random.choice(["rock", "paper", "scissors"])
user_input = input("Enter your choice - rock, paper or scissors: \n")


if(user_input == computer_choice):
    print("It's a tie, no loser here!")
elif(computer_choice=="rock" and user_input=="scissors"):
    print("You Lose! Rock beats Scissors")
elif(computer_choice=="scissors" and user_input=="paper"):
    print("You Lose! Scissors beats Paper")
elif(computer_choice=="paper" and user_input=="rock"):
    print("You Lose! Paper beats Rock")
else:
    print("You Win "+ user_input+ " beats " + computer_choice )
