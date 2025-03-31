# Program to print prime numbers less than 100

print("Prime numbers less than 100:")

for num in range(2, 100):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(num, end=" ")