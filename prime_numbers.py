def prime_numbers(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) +1):
        print(f"Id {n} divisible by {i}?")
        if n % i == 0:
            print(f"Yes, because {n} / {i} = {n//i}")
            return False
    return True

n = int(input("Enter a number: "))
if prime_numbers(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")