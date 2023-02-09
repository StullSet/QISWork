#!/usr/bin/env python3
# caesar_decrypt.py

import sys


def main(file_name, key_shift):
    # Using the manually opened file
    with open(file_name, "rb") as f_in:
        f_bytes = bytearray(f_in.read())

        # For all values in the array
        for i in range(0, len(f_bytes)):
            # Shift each element by the entered shift value
            # % 256 allows the elements that exceed 256 to jump back to 0
            f_bytes[i] = (f_bytes[i] + key_shift) % 256

        print(f_bytes.decode())


if __name__ == "__main__":
    file_name = None
    # If file not given, prompt to enter a file
    if len(sys.argv) == 1:
        print("You must provide a filename and a key value")
    # Otherwise just run
    else:
        file_name = sys.argv[1]
        key_shift = int(sys.argv[2])
        main(file_name, key_shift)
