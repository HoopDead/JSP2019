a = input("Wprowadz wartosc a: ")
b = input("Wprowadz wartosc b: ")
while a > b:
    print("Ups, cos poszlo nie tak!")
    a = input("Wprowadz wartosc a: ")
    b = input("Wprowadz wartosc b: ")

Z = int(b) % int(a)
Z *= Z+3
print(Z)

#Z * (Z+3) = Z^2 + 3Z - bez nawiasu
