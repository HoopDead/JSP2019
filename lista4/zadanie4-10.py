def nwd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print("Najwiekszy wspolny dzielnik to: ", nwd(125, 100))