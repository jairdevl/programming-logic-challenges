# Function calculate tip
def calculate_tip(account, tip_percentage, people):
    
    tip = account * (tip_percentage / 100)

    total = account + tip

    pay_people = total / people

    return tip, total, pay_people

# Ask user for the calculate tip
account = float(input("Enter the account amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
people = int(input("Enter the number of people: "))

# Calculate the tip
tip, total, pay_people = calculate_tip(account, tip_percentage, people)

# Print the results
print(f"The tip is: {tip}")
print(f"The total amount is: {total}")
print(f"Each person should pay: {pay_people}")