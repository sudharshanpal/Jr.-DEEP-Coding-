# Ceasar Cipher in Python

# https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

choice = int(input("Do you want to encrypt or decrypt? 1 = encrypt, 2 = decrypt: "))

if choice == 1:
    word = input("Please enter a word: ")
    shift = int(input("Please enter the shift value: "))
    ans = ""

    for i in range (len(word)):
        char = word[i]

        if char.isupper():
            ans += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            ans += chr((ord(char) + shift - 97) % 26 + 97)

    print("The encrypted word is: " + ans)
else:
    word = input("Please enter a word: ")
    shift = int(input("Please enter the shift value: "))
    ans = ""

    for i in range (len(word)):
        char = word[i]

        if char.isupper():
            ans += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            ans += chr((ord(char) - shift - 97) % 26 + 97)
    print("The decrypted word is: " + ans)
