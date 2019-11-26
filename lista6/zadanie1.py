import trojkat

a = int(input("Wprowadz bok A: "))
b = int(input("Wprowadz bok B: "))
c = int(input("Wprowadz bok C: "))

if (a<b+c) and (b<a+c) and (c<b+a):
    print("Warunek spelniony")
    print("Obwod trojkata: " + str(trojkat.obwod(a,b,c)))
    print("Pole trojkata: " + str(trojkat.pole(a,b,c)))
    print(trojkat.checkBoki(a,b,c))
    print(trojkat.checkTrojkat(a,b,c))
else:
    print("Warunek niespelniony")