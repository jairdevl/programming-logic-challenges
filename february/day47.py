# Convert the time

minutes = int(input("Enter the minutes: "))

hours = minutes // 60

minutes = minutes % 60

print(f"{hours} hours and {minutes} minutes")