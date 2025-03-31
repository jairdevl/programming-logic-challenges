import random 

def build_wall(word):
    # Validate initial
    if len(word) < 3 or " " in word or not word.isalpha():
        return "Invalid input"
    
    n = len(word)
    matrix = [["" for _ in range(n)] for _ in range(n)]