import sys


def fib(n):
    if n == 0:
        return n

    elif n == 1:
        return 1

    elif n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = input("n= ")

    try:
        n = int(n)
    except:
        print("n must be integer")
        sys.exit()

    if n < 0:
        print(f"{n} isn't a positive number")
        sys.exit()

    print(f"fib({n}) = {fib(n)}")
