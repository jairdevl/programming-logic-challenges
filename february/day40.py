# Program simulate launch currency serveral and count times it comes up heads or tails

import random

# Function to simulate the launch
def launch_currency(amount):
    result = {"Heads": 0, "Tails": 0}

    for i in range(amount):
        launch = random.choice(["Heads", "Tails"])
        result[launch] += 1

    return result

# Ask user for the amount of launches
amount = int(input("Enter the amount of launches: "))

# Print the result
print(launch_currency(amount))
        