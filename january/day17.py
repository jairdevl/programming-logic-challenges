# Program to count how many times a specific letter appears in a string

string = input("Enter a string: ")
letter = input("Enter a letter: ")

counter = 0

for char in string:
    if char == letter:
        counter += 1

print(f"The letter '{letter}' appears {counter} times in the string.")
