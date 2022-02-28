def max(a, b, c):
    """This function returns the max of a,b,c"""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def main():
    print(max(10,22,14))
    print(max(100,-22,14))
    print(max(0,0,1))

main()
