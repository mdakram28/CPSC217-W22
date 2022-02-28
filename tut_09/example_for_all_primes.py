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
