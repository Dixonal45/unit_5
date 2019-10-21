# by Allison Dixon
# last updated October 21, 2019
# this program plays a number guessing game with the user

import random


def main():
    while True:
        answer = input("Would you like to play a game? Answer 'y' for yes or 'n' for no.")
        if answer == "y" or answer == "n":
            break
    if answer == "y":
        print("Let's play.")
    else:
        for x in range(100):
            print("TERMINATE")


computer_num = random.randint(1, 100)

int(input("Guess the computer's number"))

main()
