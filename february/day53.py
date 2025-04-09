# Encriptado in the César message

def encrypt_cesar(message, clue):
    result = ""
    
    for char in message:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + clue) % 26
            result += chr(ord('a') + shift) if char.islower() else chr(ord('A') + shift)
        else:
            result += char
    
    return result

def decoded_cesar(encrypt_message, clue):
    return encrypt_cesar(encrypt_message, -clue)

# Aks user for input
option = input("Enter 1 to encrypt or 2 to decrypt: ")
message = input("Enter the message: ")
clue = int(input("Enter the clue: "))

if option == "1":
    print(f"Encrypted message: {encrypt_cesar(message, clue)}")
elif option == "2":
    print(f"Decrypted message: {decoded_cesar(message, clue)}")
else:
    print("Invalid option.")
