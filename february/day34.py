# Program string to palindrome
def string_to_palindrome(string):
    string = string.lower()
    return string + string[::-1]

# Ask user for a string
string = input("Enter a string: ")

# Print the result
if string_to_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
