import sys


def gcd(a, b):
    if a == 0:
        return b

    elif b == 0:
        return a

    elif a == b:
        return a

    if a > b:
        return gcd(a - b, b)

    return gcd(a, b - a)


if __name__ == "__main__":
    a = input("1st number: ")
    b = input("2nd number: ")

    try:
        a = int(a)
        b = int(b)
    except:
        print("1st and 2nd number must be integer")
        sys.exit()

    if a < 0:
        print(f"{a} isn't a positive number")
        sys.exit()
    elif b < 0:
        print(f"{b} isn't a positive number")
        sys.exit()

    print(f"gcd({a}; {b}) = {gcd(a, b)}")
