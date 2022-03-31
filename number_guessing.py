#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: March 2022
# This function takes a random integer between 0-9
# and tells the user if they guessed corretly

import random


def main():
    # this function takes a random integer between 0-9
    # and tells the user if they guessed corretly

    # input
    user_guess = int(input("Insert any number between 0-9 (integers): "))
    number = random.randint(1, 9)

    # process and output
    print("")
    if user_guess == number:
        print("Hooray you guessed correctly !! :)")
    else:
        print("Oh No!!! you guessed incorrectly :(")

    print("\nDone.")


if __name__ == "__main__":
    main()
