import math

a = float(input("Wprowadz pierwszy bok: "))
b = float(input("Wprowadz drugi bok: "))
c = float(input("Wprowadz trzeci bok: "))


first = c**2 - a**2 - b**2
second = -2*a*b
print(first)
print(second)
cos = first/second
print(cos)
print(math.degrees(math.acos((cos))))