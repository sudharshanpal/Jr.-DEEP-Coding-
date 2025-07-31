import random

word_list = ['apple', 'grape', 'mango', 'pearl', 'brick', 'plane', 'track', 'flame', 'sugar', 'heart']

secret_word = random.choice(word_list)

print("Welcome to Wordle (Simple Edition)!")
print("Guess the 5-letter word. You have 6 tries.")

tries = 6
while tries > 0:
    guess = input(f"Try {7 - tries}/6: Enter a 5-letter word: ").lower()

    if len(guess) != 5:
        print("Please enter exactly 5 letters.")
        continue

    if guess == secret_word:
        print("Congratulations! You guessed the word correctly!")
        break

    in_word = []
    not_in_word = []
    for letter in guess:
        if letter in secret_word:
            in_word.append(letter)
        else:
            not_in_word.append(letter)

    print("Letters in the word: ", " ".join(in_word) if in_word else "None")
    print("Letters NOT in the word: ", " ".join(not_in_word) if not_in_word else "None")
    tries -= 1

if tries == 0:
    print(f"Sorry, you're out of tries. The word was '{secret_word}'.")
