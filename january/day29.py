# Program generate password radmon  

import random
import string

# Define characters permitted
characters = string.ascii_letters + string.digits + string.punctuation

# Ask user for the length of the password
length = int(input("Enter the length of the password: "))

# Generate the passwords
password = ''.join(random.choice(characters) for i in range(length))

# Print the password
print(f"The generated password is: {password}")
