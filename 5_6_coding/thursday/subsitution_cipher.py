"""
Encryption and Decryption for Substitution Cipher
"""
all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message):
    key = len(message) % len(all_letters)
    dict1 = {}
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]
    cipher_txt = ""
    for char in message:
        if char in all_letters:
            cipher_txt += dict1[char]
        else:
            cipher_txt += char
    return cipher_txt

def decrypt(cipher_txt):
    key = len(cipher_txt) % len(all_letters)
    dict2 = {}
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i - key) % len(all_letters)]
    decrypt_txt = ""
    for char in cipher_txt:
        if char in all_letters:
            decrypt_txt += dict2[char]
        else:
            decrypt_txt += char
    return decrypt_txt

cipher = encrypt("I love computer science")
plain = decrypt(cipher)

with open("output.txt", "w") as file:
    file.write("Cipher Text is: " + cipher + "\n")
    file.write("Recovered plain text: " + plain + "\n")
