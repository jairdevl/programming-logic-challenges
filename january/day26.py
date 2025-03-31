# Program to invert a list

def invert_list(list):
    return list[::-1]

# Ask user for a list of numbers
list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Print the inverted list
print(f"The inverted list is: {invert_list(list)}")
