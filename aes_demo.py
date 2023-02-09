#!/usr/bin/env python3
# aes_demo.py

# Importing packages to do most of the work for us
import aes
import os


def main():
    # The secret key is 16 bytes long
    secret_key = os.urandom(16)
    print(f"Secret key = {bytearray(secret_key).hex()}\n")

    # iv = (Random) initialization vector which ensures
    # the same value encrypted multiple times, even with the
    # same secret key, will not always result in the same encrypted value
    iv = os.urandom(16)

    plaintext = b"Attack at dawn"
    print(f"plaintext = {plaintext}\n")

    # Encrypting the text
    ciphertext = aes.AES(secret_key).encrypt_ctr(plaintext, iv)
    print(f"ciphertext = {ciphertext}\n")

    # Checking to make sure nothing has changed by decrypting the text
    plaintext = aes.AES(secret_key).decrypt_ctr(ciphertext, iv)
    print(f"plaintext = {plaintext}\n")


if __name__ == "__main__":
    main()
