def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

result = gcd(48, 18)
print(result)