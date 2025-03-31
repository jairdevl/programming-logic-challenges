# Program to calculate tip and total in a restaurant
def calculate_tip(amount, tip_percentage, people):
    tip = amount * (tip_percentage / 100)
    total = amount + tip
    pay_person = total / people
    return tip, total, pay_person

# Ask user for input
amount = float(input("Enter the amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
people = int(input("Enter the number of people: "))

tip, total, pay_person = calculate_tip(amount, tip_percentage, people)

print(f"Tip: {tip}")
print(f"Total: {total}")
print(f"Pay per person: {pay_person}")

    