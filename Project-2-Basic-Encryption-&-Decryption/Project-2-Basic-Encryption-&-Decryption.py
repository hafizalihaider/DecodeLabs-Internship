'''
========================================================================
              BASIC ENCRYPTION & DECRYPTION (CAESAR CIPHER)
========================================================================

Description:
This program implements the Caesar Cipher encryption algorithm to
demonstrate basic encryption and decryption techniques.

Features:
1. Accepts a message and a shift key from the user.
2. Encrypts uppercase letters (A-Z).
3. Encrypts lowercase letters (a-z).
4. Preserves digits, spaces, and special characters.
5. Uses modular arithmetic to wrap alphabet characters.
6. Displays:
   - Original Message
   - Encrypted Message
   - Decrypted Message
7. Demonstrates that decrypting the encrypted message restores
   the original plaintext.

Algorithm:
Encryption:
    E(x) = (x + n) mod 26

Decryption:
    D(x) = (x - n) mod 26

where:
    x = Alphabet position
    n = Shift key

Author: Muhammad Ali Haider
Date: July 24, 2026
IDE: Visual Studio Code 1.129.1
Python Version: 3.14.3

========================================================================
'''

# Display the program title
print("-" * 70)
print("\n\t\t\tBasic Encryption & Decryption\n")
print("-" * 70)

# Take the original message and shift key as input
original_message = input("\nEnter Message: ")
shift_key = int(input("Enter Shift Key: "))

# Variables to store the encrypted and decrypted messages
encrypted_message = ""
decrypted_message = ""

print("-" * 70)

# Display the original message
print("\nOriginal Message: ", original_message)

# ================= Encryption =================

# Process each character in the original message
for char in original_message:

    # Convert the character into its ASCII value
    ASCII = ord(char)

    # Encrypt uppercase letters
    if ASCII >= 65 and ASCII <= 90:
        Upper_Encrypted = (ASCII - 65 + shift_key) % 26 + 65
        encrypted_message += chr(Upper_Encrypted)

    # Encrypt lowercase letters
    elif ASCII >= 97 and ASCII <= 122:
        Lower_Encrypted = (ASCII - 97 + shift_key) % 26 + 97
        encrypted_message += chr(Lower_Encrypted)

    # Keep digits, spaces and special characters unchanged
    else:
        encrypted_message += char

# Display the encrypted message
print("\nEncrypted Message: ", encrypted_message)

# ================= Decryption =================

# Process each character in the encrypted message
for char in encrypted_message:

    # Convert the encrypted character into its ASCII value
    ASCII = ord(char)

    # Decrypt uppercase letters
    if ASCII >= 65 and ASCII <= 90:
        Upper_Decrypted = (ASCII - 65 - shift_key) % 26 + 65
        decrypted_message += chr(Upper_Decrypted)

    # Decrypt lowercase letters
    elif ASCII >= 97 and ASCII <= 122:
        Lower_Decrypted = (ASCII - 97 - shift_key) % 26 + 97
        decrypted_message += chr(Lower_Decrypted)

    # Keep digits, spaces and special characters unchanged
    else:
        decrypted_message += char

# Display the decrypted message
print("\nDecrypted Message: ", decrypted_message, "\n")
print("-" * 70)