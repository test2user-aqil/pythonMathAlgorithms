def gcd(a, b):
    if a == 0:
        return b

    elif b == 0:
        return a
    
    elif a == b:
        return a

    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)

a = int(input("1st number :"))
b = int(input("2nd number :"))

print(f"GCD of {a} and {b} is {gcd(a, b)}")