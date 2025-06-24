import random

randomNum = random.randint(1, 10)
inputNum = int(input("Guess a number between 1 and 10: "))
if inputNum == randomNum:
    print("Congratulations! You guessed the right number.")
else:
    print("Sorry, the correct number was", randomNum)
# This code generates a random number between 1 and 10 and asks the user to guess it.
# If the user's guess is correct, it congratulates them; otherwise, it reveals the correct number.

# An alternate version is to use a while loop to allow multiple guesses:
# randomNum = random.randint(1, 10)
# while True:
#     inputNum = int(input("Guess a number between 1 and 10: "))
#     if inputNum == randomNum:
#         print("Congratulations! You guessed the right number.")
#         break
#     elif inputNum < randomNum:
#         print("The number is higher. Try again.")
#     elif inputNum > randomNum:
#         print("The number is lower. Try again.")
# This version continues to prompt the user until they guess the correct number.
# This code generates a random number between 1 and 10 and allows the user to guess it multiple times.
