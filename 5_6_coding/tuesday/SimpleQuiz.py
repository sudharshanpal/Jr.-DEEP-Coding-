import time

score = 0

print("Welcome to the simple quiz game!")
print("This simple quiz game will be about SpongeBob")
print("Here are the rules and instructions: ")

time.sleep(3)
print("This will be a multiple choice test based on the show SPONGEBOB")
time.sleep(2)
print("Each correct answer will give you 1 point")
time.sleep(2)

input("Are you ready? Press ENTER to start\n")

# Question 1
print("\n1. What kind of animal is SpongeBob’s best friend, Patrick?")
print("\t1. A crab")
print("\t2. A jellyfish")
print("\t3. A starfish")
print("\t4. A squid")
x = int(input("Enter your guess: "))
if x == 3:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 3. A starfish")

# Question 2
print("\n2. Where does SpongeBob work?")
print("\t1. The Chum Bucket")
print("\t2. The Krusty Krab")
print("\t3. Bikini Bottom Mall")
print("\t4. Goo Lagoon")
x = int(input("Enter your guess: "))
if x == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 2. The Krusty Krab")

# Question 3
print("\n3. What is SpongeBob’s pet snail’s name?")
print("\t1. Larry")
print("\t2. Spot")
print("\t3. Jerry")
print("\t4. Gary")
x = int(input("Enter your guess: "))
if x == 4:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 4. Gary")

# Question 4
print("\n4. Who is SpongeBob’s grumpy neighbor?")
print("\t1. Plankton")
print("\t2. Sandy")
print("\t3. Squidward")
print("\t4. Mr. Krabs")
x = int(input("Enter your guess: "))
if x == 3:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 3. Squidward")

# Question 5
print("\n5. What kind of animal is Sandy Cheeks?")
print("\t1. A squirrel")
print("\t2. A fish")
print("\t3. A rabbit")
print("\t4. A cat")
x = int(input("Enter your guess: "))
if x == 1:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 1. A squirrel")

# Question 6
print("\n6. What does SpongeBob live in?")
print("\t1. A rock")
print("\t2. A pineapple")
print("\t3. A shell")
print("\t4. A sandcastle")
x = int(input("Enter your guess: "))
if x == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 2. A pineapple")

# Question 7
print("\n7. What instrument does Squidward play?")
print("\t1. Guitar")
print("\t2. Clarinet")
print("\t3. Trumpet")
print("\t4. Flute")
x = int(input("Enter your guess: "))
if x == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 2. Clarinet")

# Final Score
print("\nQuiz complete!")
print(f"Your final score is: {score}/7")
if score == 7:
    print("Amazing! You're a SpongeBob expert!")
elif score >= 4:
    print("Good job! You know your SpongeBob pretty well.")
else:
    print("Nice try! Maybe watch a few more episodes!")

