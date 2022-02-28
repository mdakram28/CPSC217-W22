
for number in range(2, 100):
    # The number is assumed to be prime
    is_prime = True
    for i in range(2, int(number/2 + 1)):
        if number % i == 0:
            is_prime = False
            break

    # Print result
    if is_prime:
        print(number)
