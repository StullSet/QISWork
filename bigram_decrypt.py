#!/usr/bin/env python3
# bigram_decrypt.py

import os
import sys


def main():
    # Requiring algorithm to read bigram_ciphertext
    in_file = os.path.dirname(sys.argv[0]) + "/bigram_ciphertext.txt"
    key_xor = 128

    with open(in_file, "rb") as f_in:
        # Converting read file to byte array
        f_bytes = bytearray(f_in.read())

        for i in range(0, len(f_bytes)):
            # Shifter all elements based on our key
            # In this case we raise the element to the keys power
            f_bytes[i] = f_bytes[i] ^ key_xor

        print(f_bytes.decode())


if __name__ == "__main__":
    main()
