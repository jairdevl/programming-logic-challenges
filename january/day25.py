# Function that receives a list of numbers and returns the sum of its elements
def sum_elements(list):
    return sum(list)

# Ask user for a list of numbers
list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Print the sum of the list
print(f"The sum of the list is: {sum_elements(list)}")