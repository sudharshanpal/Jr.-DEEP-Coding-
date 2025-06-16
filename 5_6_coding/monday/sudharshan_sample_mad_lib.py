"""
Mad Libs Generator - Jr. DEEP Coding Sample Project

This program creates a fun and interactive Mad Libs story by asking the user
to input various types of words (e.g., nouns, verbs, adjectives). The inputs
are then inserted into a pre-defined story template to generate a humorous and
personalized narrative.
"""
# Collect user input
adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb_past = input("Enter a verb (past tense): ")
emotion = input("Enter an emotion: ")
game = input("Enter a sport or game: ")
food = input("Enter a type of food: ")
place = input("Enter a place: ")
adj2 = input("Enter another adjective: ")
celebrity = input("Enter a celebrity or fictional character: ")
noun2 = input("Enter a noun: ")

# The story
print("\n--- Sudharshan's Mad Lib Story ---\n")
print(f"Meet Sudharshan, a {adj1} second-year computer science student at the University of Toronto.")
print(f"He spends his days juggling {noun1}, solving math problems, and writing code that once {verb_past} an entire program.")
print(f"When he's not debugging, he's playing chess, watching the Oilers, or feeling incredibly {emotion} about a close game of {game}.")
print(f"His favorite snack after a long study session is {food}, preferably shared with friends at {place}.")
print(f"On weekends, you’ll find him lifting weights while listening to an {adj2} playlist, or binge-watching Avatar: The Last Airbender.")
print(f"One day, Sudharshan hopes to build a tech tool so helpful that even {celebrity} would use it.")
print(f"Until then, he’ll keep learning, playing basketball, and eating way too much {noun2}.")
