def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
text = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

if choice == "encrypt":
    print("Encrypted message:", encrypt(text, shift))
elif choice == "decrypt":
    print("Decrypted message:", decrypt(text, shift))
else:
    print("Invalid choice!")
