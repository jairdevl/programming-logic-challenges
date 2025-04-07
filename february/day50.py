# Program to find the longest word in a text

sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print(f"The longest word in the sentence is: {longest_word}")
