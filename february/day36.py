# Program that generate a random 1 to 100 and ask user to guess it

import random

number = random.randint(1, 100)

intents = 0

while True:
    guess = int(input("Enter your guess: "))
    intents += 1
    if guess < number:
        print("Too low")
    else:
        print("Too high")

    if guess == number:
        print(f"Congratulations! You guessed the number in {intents} attempts.")
        break