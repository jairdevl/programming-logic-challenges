# Function combine two lists and sum the elements

def combine_and_sum(list1, list2):
    return sum(list1 + list2)

# Ask user for two lists of numbers
list1 = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Print the sum of the combined list
print(f"The sum of the combined list is: {combine_and_sum(list1, list2)}")