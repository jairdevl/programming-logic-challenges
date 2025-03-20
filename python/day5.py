# Basic arithmetic operations (addition, subtraction, multiplication, división) with numbers entered by the user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

print(f"The addition of {num1} and {num2} is: {addition}")
print(f"The subtraction of {num1} and {num2} is {subtraction}")
print(f"The multiplication of {num1} and {num2} is {multiplication}")
print(f"The division of {num1} and {num2} is: {division}")