def count_words(text):
    text = text.split()
    return len(text)

text = input("Enter your text: ")
print(f"Number of words: {count_words(text)}")
