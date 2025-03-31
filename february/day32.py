# Program find number eldeled and minor list 

# Ask user for a list of numbers
list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Find max number
max_number = max(list)

# Find min number
min_number = min(list)

# Print the max and min numbers
print(f"The largest number is: {max_number}")
print(f"The smallest number is: {min_number}")