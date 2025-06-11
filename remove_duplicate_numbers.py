def remove_duplicate_numbers(list):
    unique = []
    for num in list:
        if num not in unique:
            unique.append(num)
    return unique

list = [3, 5, 3, 7, 5,9]
print(remove_duplicate_numbers(list))

