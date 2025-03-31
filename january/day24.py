# Function that generates a list of random numbers

import random

def generate_random_numbers(n, start, end):
    return [random.randint(start, end) for _ in range(n)]

# Ask user for the number of random numbers and the range
n = int(input("Enter the number of random numbers: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Generate and print the list of random numbers
random_numbers = generate_random_numbers(n, start, end)
print(f"The list of {n} random numbers between {start} and {end} is: {random_numbers}")