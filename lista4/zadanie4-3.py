import math

print("Podaj, czy radiany czy stopnie. (1 - radiany, 2 - stopnie")

a = int(input("Wprowadz: "))

def convert(arg, option):
    if (option == 1):
        return arg * (180/math.pi)
    if(option == 2):
        return arg * (math.pi/180)

if a == 1:
    b = int(input("Wprowadz radiany: "))
    print(convert(b, 1), "stopni")
elif a == 2:
    b = int(input("Wprowadz stopnie: "))
    print(convert(b, 2), "rad")
elif a > 2 and a < 0:
    print("Wprowadziles cos zle!")
