def palidrome(text_string):
    text = text_string.lower().replace(" ","")
    return text == text[::-1]

text_string = input("Enter a text string: ")
if palidrome(text_string):
    print("It's a palindrome!")
else:
    print("It's not a prlindrome!")