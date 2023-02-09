#!/usr/bin/env python3
# bigram_frequency.py

from collections import Counter
import os
import sys


def main():
    # Manually requiring the program to open bigram_ciphertext.txt
    file_name = os.path.dirname(sys.argv[0]) + "/bigram_ciphertext.txt"
    with open(file_name, "rb") as f_in:
        print(f'Bigram analysis of file \n"{file_name}" :')

        # Read in text file into an array of file bytes
        f_bytes = bytearray(f_in.read())

        # Create Counter dictionary storing successive letter counts
        bigrams = Counter()
        for i in range(0, len(f_bytes) - 2):
            bigrams[(f_bytes[i], f_bytes[i + 1])] += 1

        # Normalize frequency of each bigram against total number of bigrams
        num_bigrams = sum(bigrams.values())
        for k in bigrams:
            bigrams[k] = bigrams[k] / num_bigrams

        # Reverse sort bigram frequency dictionary by values (not keys) kv[1],
        # so the bigrams with the highest normalized frequency appear first
        sorted_bigrams = sorted(bigrams.items(), key=lambda kv: kv[1], reverse=True)

        # Print the top 10 most frequently occurring bigrams in text file
        for k, v in sorted_bigrams[:10]:
            # Convert key tuple to ASCII string
            s = "".join(map(chr, k))
            print(f'Bigram {k}, "{s}": freq = {v:>5.2%}')


if __name__ == "__main__":
    main()
