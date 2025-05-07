def zeller_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    
    q = day
    m = month
    k = year % 100
    j = year // 100
    h = (q +(13*(m+1))// 5 + k + k//4 + j//4-2*j)%7
    return h

print(f"h= {zeller_congruence(6, 9, 2010)}")