




def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for number in range(1, 100, 2):
    # Print result
    if check_prime(number):
        print(number)
