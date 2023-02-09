#!/usr/bin/env python3
# board_encoding.py

import numpy as np


def ternary_convert(n):
    # Creating a list of 9 zeros to later be replaced
    remainders = 9 * [0]
    count = 0

    # While n does not equal zero proceed through loop
    while n != 0:
        # Calculate the floor and remainder using base 3 conversions
        # And assigning the remainder to it's position in the list
        remainders[count] = n % 3

        # Updating n and moving to the next list element
        n = n // 3
        count += 1

    return remainders


def main():
    # Establishing the 3 required n values
    # n = 2271
    n = 1638
    # n = 12065

    # Initializing variable to help turn the list into the expected board
    # This process converts the list into an array and then presents it
    # similar to a 3x3 matrix. More specifically 3 arrays with 3 elements
    shape = (3, 3)
    board = np.array(ternary_convert(n)).reshape(shape)

    # \n moves print text down to the next line
    print(f"Board Number: {n} \n {board}")


# Same main function we've typically used
if __name__ == "__main__":
    main()
