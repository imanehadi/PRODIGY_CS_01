Caesar Cipher Project
Overview

This is a simple Python program that implements the Caesar Cipher algorithm. The program allows users to encrypt and decrypt text messages by shifting letters by a specified value.

It is built as a small educational project to understand basic encryption techniques and Python programming concepts like functions, loops, and string manipulation.

Features

Encrypt any text message with a user-defined shift value.

Decrypt any encrypted text using the same shift value.

Handles both uppercase and lowercase letters.

Non-alphabetic characters (numbers, punctuation, spaces) remain unchanged.

User-friendly input prompts for encryption or decryption.

How to Run

Clone or download the repository.

Open a terminal in the project folder.

Run the program using Python 3:

python3 caesar_cipher.py


Follow the prompts:

Type encrypt to encrypt a message or decrypt to decrypt.

Enter your message.

Enter the shift number.

Example

Encryption:

Type 'encrypt' to encrypt or 'decrypt' to decrypt: encrypt
Enter your message: Hello World
Enter the shift number: 3
Encrypted message: Khoor Zruog


Decryption:

Type 'encrypt' to encrypt or 'decrypt' to decrypt: decrypt
Enter your message: Khoor Zruog
Enter the shift number: 3
Decrypted message: Hello World

Installation Requirements

Python 3.x
No external libraries are required.

Project Structure
caesar_cipher_project/
│
├── caesar_cipher.py       # Main Python program
├── README.md              # Project documentation


Knowledge Gained

Understanding of classical encryption techniques.

Practice with Python string manipulation and ASCII operations.

Writing user-interactive command-line applications.
