def compound_interest(principal, rate, time):
    """This function will return the compound interest on the principal amount"""
    amount = principal * (pow((1 + rate / 100), time))
    interest = amount - principal
    return interest

amount = float(input("Enter the invested amount"))
rate = 14
years = 8
ci = compound_interest(amount, rate, years)
print("{0} will yield an interest of {1:.2f} in {2} years".format(amount, ci, years))
