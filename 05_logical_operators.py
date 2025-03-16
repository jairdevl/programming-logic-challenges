"""
Logical operators AND, OR, NOT
"""

x = int(input("Enter one number: "))
y = int(input("Enter another number: "))

# AND
if x > 0 and y > 0:
    print("Both x and y are positive.")

# OR
if x > 0 or y > 0:
    print("At least one of x or y is positive.")

# NOT
if not x > 0:
    print("x is not positive.")

