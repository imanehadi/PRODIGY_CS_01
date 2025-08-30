# Image Encryptor via Pixel Manipulation

This is a simple **educational project** that demonstrates image encryption and decryption using **pixel manipulation** in Python.  
It allows you to **encrypt images** by shuffling pixel positions and/or applying XOR with a pseudorandom keystream, and then **decrypt them back** to the original.

> ⚠️ This project is for learning purposes only and is **not cryptographically secure**.

---

##  Features

- Encrypt images using:
  - **XOR**: Pixel values are XORed with a pseudorandom keystream derived from a passphrase.
  - **Shuffle**: Pixel positions are permuted pseudorandomly.
  - **Both**: Shuffle then XOR.
- Decrypt images back to their original form.
- Command-line interface (CLI) for easy usage.

---

##  Requirements

- **Python 3.10+**
- Libraries:
  - `Pillow` (for image handling)
  - `numpy` (for pixel manipulation)

---

##  Installation (Ubuntu)

1. **Update packages**:
   ```bash
   sudo apt update
sudo apt install python3 python3-pip -y
pip install pillow numpy
##  Usage

1. Run the program:
   ```bash
   python3 image_encryptor.py
   
Type 'encrypt' to encrypt or 'decrypt' to decrypt: encrypt
Enter the image path: input/photo.png
Enter your passphrase: mySecret123
Choose method (xor/shuffle/both): both
Encrypted image saved to: output/photo_encrypted.png

Type 'encrypt' to encrypt or 'decrypt' to decrypt: decrypt
Enter the image path: output/photo_encrypted.png
Enter your passphrase: mySecret123
Choose method (xor/shuffle/both): both
Decrypted image saved to: output/photo_decrypted.png


