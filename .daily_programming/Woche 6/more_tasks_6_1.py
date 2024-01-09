# 2 Prime Number Checker:

import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Get user input for the number to check for primality
num_to_check = int(input("Enter a number to check for primality: "))
result = is_prime(num_to_check)

if result:
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")