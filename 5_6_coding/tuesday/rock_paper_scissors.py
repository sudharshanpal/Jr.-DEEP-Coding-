"""
Rock, Paper, Scissors - Jr. DEEP Coding Sample Activity

This program simulates a Rock, Paper, Scissors game where the user plays against the computer.
The user is repeatedly prompted to choose 'rock', 'paper', or 'scissors' (or 'quit' to end the game),
while the computer makes a random selection each round. The program determines the winner of each round,
updates the score accordingly, and displays the results in real time. This activity helps reinforce
core programming concepts such as loops, conditionals, user input validation, and randomization
in a fun and engaging way.
"""
import random

answer = ""
user_score = 0
bot_score = 0

while answer != 'quit':
    answer = input("Choose rock paper or scisscors: ")
    options = ['rock', 'paper', 'scissors', 'quit']

    while answer not in options:
        answer = input("Pick a valid option: ")

    x = random.randint(0, 3)
    if answer == options[x]:
        print("computer chose " + options[x])
        print("game has drawn")
        continue
    elif answer == "paper" and options[x] == "rock" or answer == "rock" and options[x] == "scissors" or answer == "scissors" and options[x] == "paper":
        user_score += 1
        print("computer chose " + options[x])
        print(f"you WON! Your score is {user_score} and the computer's score is {bot_score}")
        continue
    elif answer != 'quit':
        bot_score += 1
        print("computer chose " + options[x])
        print(f"you LOST! Your score is {user_score} and the computer's score is {bot_score}")
        continue
