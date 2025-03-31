# Program calculate media numbers
def calculate_media(numbers):
    return sum(numbers) / len(numbers)

# Ask user for a list of numbers
list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Print the media of the list
print(f"The media of the list is: {calculate_media(list)}")
