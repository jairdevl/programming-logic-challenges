# Program to calculate the average of n notes       

n = int(input("Enter the number of notes: "))

notes = []

for i in range(n):
    note = float(input(f"Enter the {i+1} note: "))
    notes.append(note)

average = sum(notes) / n

print(f"The average of {notes} is: {average}")