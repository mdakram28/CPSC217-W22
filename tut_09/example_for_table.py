number = int(input("Enter an integer: "))

# Count from 1 to 10
for count in range(1, 11):
    product = number * count
    print("{0} x {1} = {2}".format(number, count, product))
