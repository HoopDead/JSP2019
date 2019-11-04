n = int(input("Wprowadz n: "))
a1 = int(input("Wprowadz pierwszy wyraz: "))

def ciag(q, n, a1):
    return a1 * q**(n-1)

print("Wyraz na n-tym miejscu to: ", ciag(2, n, a1))