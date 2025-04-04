<<<<<<< HEAD
# Program which counts how many times each word appears in a text
def count_words(text):
    words =  text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
# Ask user text
text = input("Enter a text: ")

# Count words and print result
word_count = count_words(text)
print(word_count)
=======
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
>>>>>>> c0cf94b5a757f83913cb90cb71ce6a7ec32cd777
