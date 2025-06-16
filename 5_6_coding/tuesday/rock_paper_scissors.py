import random

answer = input("Choose rock paper or scisscors: ")
options = ['rock', 'paper', 'scissors']

while answer not in options:
    answer = input("Pick a valid option: ")

x = random.randint(0, 3)
print("computer chose " + options[x])
if answer == options[x]:
    print("game has drawn")
elif answer == "paper" and options[x] == "rock" or answer == "rock" and options[x] == "scissors" or answer == "scissors" and options[x] == "paper":
    print("you WON!")
else:
    print("you LOST!")
