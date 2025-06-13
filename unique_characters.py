def unique_characters(text_string):
    text_string = text_string.replace(" ", "")
    return len(set(text_string)) == len(text_string)

text_string = input("Enter a text string: ")
if unique_characters(text_string):
    print("All characters are unique")
else:
    print("There are repeated characters")