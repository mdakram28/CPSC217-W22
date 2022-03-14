


def maximum(a, b, c):
    """This function returns the max of a,b,c"""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def main():
    print(maximum(10,22,14))
    print(maximum(100,-22,14))
    print(maximum(0,0,1))

main()
