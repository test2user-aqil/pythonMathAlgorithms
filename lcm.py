import sys


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


if __name__ == "__main__":
    a = input("1st number : ")
    b = input("2nd number : ")

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

    print(f"lcm({a}; {b}) = {lcm(a, b)}")
