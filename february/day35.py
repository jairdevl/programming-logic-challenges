<<<<<<< HEAD
# Program that count how many words has a phrase

phrase = input("Enter a phrase:")

words = phrase.split()

print(f"The phrase has {len(words)} words.")
=======
# Program to count words in the phrase

def count_words(phrase):
    return len(phrase.split())

phrase = input("Enter a phrase: ")

print(f"The phrase has {count_words(phrase )} words")
>>>>>>> c0cf94b5a757f83913cb90cb71ce6a7ec32cd777
