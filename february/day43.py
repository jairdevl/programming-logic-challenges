# Function that converts a person's age into days

def age_to_days(age):
    return age * 365

# Ask user for age
age = int(input("Enter your age: "))

# Print the result
print(f"Your age in days is: {age_to_days(age)}")