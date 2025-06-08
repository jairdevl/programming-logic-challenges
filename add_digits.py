def add_digits(number):
    if number < 0:
        return "The entered number must be positive."
    else:
        addition = 0
        for digit in str(number):
            addition += int(digit)
        return addition

number = int(input("Enter a positive integer: "))
print(add_digits(number))