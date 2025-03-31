# Program to count words in a list has exact 3 letters

words = ["cat", "dog", "bird", "fish", "ant"]

letters_3 = [word for word in words if len(word)]

print(f"There is/are {len(letters_3)} word/words with 3 letters")