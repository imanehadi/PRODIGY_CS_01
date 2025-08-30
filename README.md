#  Caesar Cipher Project

This is a simple **Python program** that implements the **Caesar Cipher** algorithm.  
It allows users to **encrypt and decrypt text messages** by shifting each letter by a specified number of positions in the alphabet.  

This project is created for **educational purposes** to practice Python basics such as functions, loops, conditionals, and string manipulation.  

---

##  Features

-  **Encrypt** text with a user-defined shift value.  
-  **Decrypt** text using the same shift value.  
-  Supports both **uppercase and lowercase letters**.  
-  Keeps non-alphabetic characters unchanged (numbers, punctuation, spaces).  
-  User-friendly command-line interface (CLI).  

---

##  Requirements

- **Python 3.x**  
- No external libraries are required.  

---

##  Installation (Ubuntu)

1. **Update packages**:
   ```bash
   sudo apt update
   sudo apt install python3 -y
   python3 caesar_cipher.py

Type 'encrypt' to encrypt or 'decrypt' to decrypt: encrypt
Enter your message: Hello World
Enter the shift number: 3
Encrypted message: Khoor Zruog

Type 'encrypt' to encrypt or 'decrypt' to decrypt: decrypt
Enter your message: Khoor Zruog
Enter the shift number: 3
Decrypted message: Hello World

 


