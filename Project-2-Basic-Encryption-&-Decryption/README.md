# Basic Encryption & Decryption (Caesar Cipher)

A simple Python implementation of the Caesar Cipher developed during my **DecodeLabs Cyber Security Internship**.

## Overview

This project demonstrates the fundamentals of classical cryptography by implementing the Caesar Cipher algorithm. It encrypts alphabetic characters using a user-defined shift key and then decrypts the encrypted message back to its original form.

## Features

- Encrypts uppercase letters (A–Z)
- Encrypts lowercase letters (a–z)
- Preserves digits, spaces, and special characters
- Supports user-defined shift keys
- Performs both encryption and decryption
- Uses modular arithmetic for alphabet wrapping

## Technologies Used

- Python 3.14
- Visual Studio Code

## Algorithm

### Encryption

```
E(x) = (x + n) mod 26
```

### Decryption

```
D(x) = (x - n) mod 26
```

Where:

- **x** = Alphabet position
- **n** = Shift key

## Example

**Input**

```
Message : Hello World!
Shift   : 3
```

**Output**

```
Original Message : Hello World!
Encrypted Message: Khoor Zruog!
Decrypted Message: Hello World!
```

## Learning Outcomes

- Character encoding using ASCII
- `ord()` and `chr()` functions
- String manipulation
- `for` loops
- Conditional statements
- Modular arithmetic
- Basic cryptography concepts

## Author

**Muhammad Ali Haider**

DecodeLabs Cyber Security Internship