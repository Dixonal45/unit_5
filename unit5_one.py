# by Allison Dixon
# last updated October 22, 2019
# this program plays a number guessing game with the user

import random


def main():
    # this while True statement makes it possible for the user to play multiple times
    while True:
        # this while True statement asks and responds to if the user wants to play the game
        while True:
            answer = input("Would you like to play a game? Answer 'y' for yes or 'n' for no.")
            if answer == "y" or answer == "n":
                break
        if answer == "y":
            print("Let's play.")
        else:
            print("bye bye")
            break
        computer_num = random.randint(1, 100)
        tries = 0
        # this while True statement allows the user to guess the number and responds; it also counts the tries
        while True:
            guess = int(input("Guess the computer's number between one and a hundred."))
            tries += 1
            if computer_num == guess:
                print("Way to go, you got it right.")
                break
            elif guess >= 100 or guess <= 0:
                print("Make sure your guess is in the right range.")
            elif guess > computer_num:
                print("Too high.")
            else:
                print("Too low.")
        print("It took you", tries, "to guess the number.")


main()
