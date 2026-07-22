'''
========================================================================
                    PASSWORD STRENGTH CHECKER
========================================================================

Description:
This program evaluates the strength of a password using the following
rules:

1. Password length must be between 8 and 16 characters.
2. Password must not contain any spaces.
3. The password is checked for the following character types:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Digits (0-9)
   - Special characters (!, @, #, $, %, etc.)
4. The number of character types present is counted.
5. The program detects predictable sequential patterns:
   - Numeric sequences of three consecutive digits
   - Reverse numeric sequences
   - Uppercase alphabet sequences
   - Reverse uppercase alphabet sequences
   - Lowercase alphabet sequences
   - Reverse lowercase alphabet sequences
6. Password strength is classified as Weak, Medium or Strong.
7. Missing character types are reported.
8. Passwords with invalid length or spaces are flagged.

Author: Muhammad Ali Haider
Date: July 20, 2026
IDE: Visual Studio Code 1.129.1
Python Version: 3.14.3

========================================================================
'''

# ========================================================================
# DISPLAY PROGRAM TITLE
# ========================================================================

print("-"*70)
print("\n\t\t\tPassword Strength Checker\n")
print("-"*70)

# ========================================================================
# USER INPUT
# ========================================================================

password = input("\nEnter your password: ")

# ========================================================================
# PASSWORD ANALYSIS
# ========================================================================

length = len(password)

has_digit = any(char.isdigit()
                for char in password)

has_upper = any(char.isupper()
                for char in password)

has_lower = any(char.islower()
                for char in password)

has_special = any(not char.isalnum()
                  for char in password)

has_space = any(char.isspace()
                for char in password)

print("-"*70)

# ========================================================================
# INITIALIZE VARIABLES
# ========================================================================

types_count = 0
sequences_count = 0

digit_sequence = "1234567890"
U_alphabets_sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L_alphabets_sequence = "abcdefghijklmnopqrstuvwxyz"

found_sequences = []

# ========================================================================
# COUNT CHARACTER TYPES
# ========================================================================

if has_digit:
    types_count += 1

if has_upper:
    types_count += 1

if has_lower:
    types_count += 1

if has_special:
    types_count += 1

# ========================================================================
# DETECT PREDICTABLE SEQUENCES
# ========================================================================

for i in range(8):
    piece = digit_sequence[i:i+3]
    if piece in password:
        sequences_count += 1
        found_sequences.append(piece)

for i in range(8):
    piece = digit_sequence[i:i+3][::-1]
    if piece in password:
        sequences_count += 1
        found_sequences.append(piece)

for i in range(24):
    piece = U_alphabets_sequence[i:i+3]
    if piece in password:
        sequences_count += 1
        found_sequences.append(piece)

for i in range(24):
    piece = U_alphabets_sequence[i:i+3][::-1]
    if piece in password:
        sequences_count += 1
        found_sequences.append(piece)

for i in range(24):
    piece = L_alphabets_sequence[i:i+3]
    if piece in password:
        sequences_count += 1
        found_sequences.append(piece)

for i in range(24):
    piece = L_alphabets_sequence[i:i+3][::-1]
    if piece in password:
        sequences_count += 1
        found_sequences.append(piece)

# ========================================================================
# DETERMINE PASSWORD STRENGTH
# ========================================================================

if types_count <= 2 or sequences_count >= 2:
    print("\nPassword Strength: Weak\n\n")

elif types_count == 3 or sequences_count == 1:
    print("\nPassword Strength: Medium\n\n")

elif types_count == 4:
    print("\nPassword Strength: Strong\n\n")

# ========================================================================
# DISPLAY REMARKS
# ========================================================================

print("Remarks:\n")

if length < 8 or length > 16:
    print("✗  Password length must be between 8 and 16 characters.")
else:
    print("✓  Password length is valid (8–16 characters).")

if has_space:
    print("✗  Spaces are not allowed.")
else:
    print("✓  No spaces detected.")

if not has_upper:
    print("✗  Missing uppercase letter(s).")
else:
    print("✓  Contains uppercase letter(s).")

if not has_lower:
    print("✗  Missing lowercase letter(s).")
else:
    print("✓  Contains lowercase letter(s).")

if not has_digit:
    print("✗  Missing digit(s).")
else:
    print("✓  Contains digit(s).")

if not has_special:
    print("✗  Missing special character(s).")
else:
    print("✓  Contains special character(s).")

if sequences_count > 0:
    print(f"✗  {sequences_count} predictable sequence(s) detected.")
    for sequence in found_sequences:
        print("     •", sequence)
else:
    print("✓  No predictable sequence(s) detected.")

# ========================================================================
# END OF PROGRAM
# ========================================================================

print("-"*70)