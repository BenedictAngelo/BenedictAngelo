import string
import random

chars = string.digits + string.ascii_letters + string.punctuation + " "
chars = list(chars)
key = chars.copy()


random.shuffle(key)

#print(chars)
#print(key)

# Encrypt

plain_text = input("Enter your message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Here is the plain message: {plain_text}")
print(f"Here is the cipher message: {cipher_text}")

# Decrypt

cipher_text = input("Enter your message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Here is your encrypted message: {cipher_text}")
print(f"Here is the decrypted message: {plain_text}")

