a = int(input("Wprowadz a: "))
b = int(input("Wprowadz b: "))
c = int(input("Wprowadz c: "))


if(a == 0):
    print("Wprowadziles zly wspolczynnik a!")
delta_sqrt = ((b**2) - 4*(a*c))**(0.5)
b = -b
print("Pierwsze miejsce zerowe: ", ((b-delta_sqrt)/2*a))
print("Drugie miejsce zerowe: ", ((b+delta_sqrt)/2*a))
