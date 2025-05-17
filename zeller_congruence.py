# Zeller's Congruence Algorithm
def zeller_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    
    # Variable keys
    q = day
    m = month
    k = year % 100
    j = year // 100

    # Main formula
    h = (q +(13*(m+1))// 5 + k + k//4 + j//4-2*j)%7

    # Mapping the days of the week
    days = ["sábado", "Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    return days[h]

# Ask user for data
try:
    day = int(input("Enter the day (1-31): "))
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (ej. 2025): "))

    # Get the day of the week
    day_name = zeller_congruence(day, month, year)

    if day_name:
        print(f"The day {day}/{month}/{year} is {day_name}")
    else:
        print("¡Invalid date. Please enter a valid date")
except ValueError:
    print("Error: Please enter valid numbers")