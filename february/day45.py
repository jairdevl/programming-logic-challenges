# Program that generates a personalize romantic message
import random

def generate_message():
    messages = [
        "You are the best person I have ever met.",
        "I am so lucky to have you in my life.",
        "You make my day brighter with your presence.",
        "I love you more than words can express.",
        "You are the light of my life.",
        "I am so grateful to have you in my life.",
        "You are the reason I smile every day.",
        "I am so lucky to have you by my side.",
        "You are the best thing that has ever happened to me.",
        "I am so lucky to have you in my life.",
    ]
    return random.choice(messages)

if __name__ == "__main__":
    # Ask user for their name
    name = input("Enter your name: ")
    print(f"{generate_message()}, {name}!")