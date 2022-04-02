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
    number_as_string = input("Insert any number between 0-9: ")
    user_number = random.randint(1, 9)
    # process and output
    print("")
    try:
        number_as_integer = int(number_as_string)
        if number_as_integer == user_number:
            print("Hooray you guessed correctly !! :)")
        else:
            print("Oh No!!! you guessed incorrectly :(")
    except Exception:
        print("Really? (-_-)ゞ pick a Integer pls ")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
