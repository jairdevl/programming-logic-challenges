# Program count how many times each word appears in a phrase
def count_words(phrase):
    word_count = {}
    words = phrase.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Ask user for a phrase
phrase = input("Enter a phrase: ")

# Print the word count
print(count_words(phrase))