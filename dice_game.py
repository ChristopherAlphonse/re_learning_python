import random


def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"({dice1}, {dice2}) ")
    total = dice1 + dice2
    return total


def main():
    player_one = input("Enter player one name: \n")
    player_two = input("Enter player two name: \n")
    player_one_roll = roll()
    player_two_roll = roll()

    print(f"{player_one} rolled {player_one_roll}")
    print(f"{player_two} rolled {player_two_roll}")

    if player_one_roll > player_two_roll:
        print(f"{player_one} wins!")
    elif player_one_roll < player_two_roll:
        print(f"{player_two} wins!")
    else:
        print("It a TIE!")


main()
