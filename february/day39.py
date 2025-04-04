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