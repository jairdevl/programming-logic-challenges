# Program to calculate total vocals in a string 

string = input("Enter a string: ")

vocals = 'aeiouAEIOU'

count = 0

for char in string:
    if char in vocals:
        count += 1

print(f"The total vocals in the string is: {count}")
