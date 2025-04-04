<<<<<<< HEAD
# Program that generate a random 1 to 100 and ask user to guess it
=======
# Program generate number random 1 to 100 and ask user guess it
>>>>>>> c0cf94b5a757f83913cb90cb71ce6a7ec32cd777

import random

number = random.randint(1, 100)

intents = 0

<<<<<<< HEAD
while True:
    guess = int(input("Enter your guess: "))
    intents += 1
    if guess < number:
        print("Too low")
    else:
        print("Too high")

    if guess == number:
=======
print("Welcome to the number guessing game!")
print("I have guessed a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    intents += 1

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
>>>>>>> c0cf94b5a757f83913cb90cb71ce6a7ec32cd777
        print(f"Congratulations! You guessed the number in {intents} attempts.")
        break