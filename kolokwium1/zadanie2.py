x = float(input("Podaj wartosc x: "))
a = []

ax = 0

print("Wprowadzenie wartosci 'koncz' konczy dzialanie petli i przekazuje do funkcji wielomian")

def wielomian(x, a):
    suma = 0
    potega = 0
    for i in a:
        suma += (i*(x**potega))
        potega += 1
    return suma

while(ax != 'koncz'):
    ax = input("Wprowadz ax (Wprowadzanie od najmniejszej potęgi, czyli wyrazu wolnego, po największą): ")
    if(str(ax) == 'koncz'):
        break
    elif type(float(ax) == ax or type(int(ax)) == int):
        a.append(float(ax))


print("Wartość wielomianu w danym punkcie to: ", wielomian(x, a))