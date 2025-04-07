# Guess the hidden word

import random

word = ["python", "java", "c++", "javascript", "ruby"]

word_hidden = random.choice(word)

hidden_word = "_" * len(word_hidden)

intentos = 10

print("You have 10 attempts to guess the hidden word.")
print("".join(hidden_word))

while "_" in hidden_word and intentos > 0:
    char = input("Enter a letter: ").lower()
    
    if char in word_hidden:
        for i in range(len(word_hidden)):
            if word_hidden[i] == char:
                hidden_word[i] = char
        
    else:
        intentos -= 1
        print(f"Wrong letter. You have {intentos} attempts left.")
    
    print("".join(hidden_word))
    
if "_" not in hidden_word:
    print(f"Congratulations! You guessed the word: {word_hidden}")
else:
    print(f"Game over! The hidden word was: {word_hidden}")
