def count_vowels_consonants(string_text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    num_consonants = 0
    for char in string_text.lower():
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return num_vowels, num_consonants

string_text = input("Enter your text: ")
v, c = count_vowels_consonants(string_text)
print(f"Vowels: {v}")
print(f"Consonants: {c}")