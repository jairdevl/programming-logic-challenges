# Order list of numbers using sort(). Ask user for numbers for the list

numbers = []

print("Welcome to the number sorter!")

n = int(input("Enter the number of numbers: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.sort()

print(f"The sorted list of numbers is: {numbers}")
