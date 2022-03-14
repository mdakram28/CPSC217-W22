



"""
Exercise
Convert the program to print all prime numbers to use a function.
Create the function to check if a number is prime or not if needed.

Starting code: tut_09/example_for_all_primes.py
"""

for number in range(1, 100, 2):
    # The number is assumed to be prime
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    # Print result
    if is_prime == True:
        print(number)
