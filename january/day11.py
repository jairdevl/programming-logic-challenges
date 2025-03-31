# Program to guess a number

import random

number = random.randint(1, 100)

intents = 0

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
        print(f"Congratulations! You guessed the number in {intents} attempts.")
        break


