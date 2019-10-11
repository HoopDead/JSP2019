a = input("Wprowadz wartosc a: ")
b = input("Wprowadz wartosc b: ")
while a > b:
    print("Ups, cos poszlo nie tak!")
    a = input("Wprowadz wartosc a: ")
    b = input("Wprowadz wartosc b: ")

Z = int(b) % int(a)
print(Z**2 + 3*Z)

#Z * (Z+3) = Z^2 + 3Z - bez nawiasu