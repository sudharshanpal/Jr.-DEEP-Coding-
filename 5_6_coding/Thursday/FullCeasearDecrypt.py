# this code will decrypt any phrase without knowing the key

word = input("Enter the word you want to decrypt (you dont know the key): ")

for i in range(1, 26):
    shift = i
    ans = ""

    for j in range(len(word)):
        char = word[j]

        if char.isupper():
            ans += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            ans += chr((ord(char) - shift - 97) % 26 + 97)
    print("Using the shift " + str(shift) + ", the decrypted word is: " + ans)
