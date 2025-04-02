# Program to count words in the phrase

def count_words(phrase):
    return len(phrase.split())

phrase = input("Enter a phrase: ")

print(f"The phrase has {count_words(phrase )} words")