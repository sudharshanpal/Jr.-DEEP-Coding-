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

print(encrypt("Hello how are you doing today"))

print(decrypt('kHOOR KRZ DUH bRX GRLQJ WRGDb'))
