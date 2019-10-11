import math

print(11//6)
print(round(5.5))
print(math.floor(5.5))

#Operacja x//y zawsze zaokrągla do pełnych całości, nawet jeżeli mamy 11//6, gdzie brakuje jedynie jednej liczby do pełnej całości, to python
#zaokrągli w dół. Funkcja round zaokrągla według matematycznych wytycznych - x.0 do x.4 zaokrągla w dół, x.5 i większe w góre. Funkcja floor zaorkągla
#zawsze w dół, niezależnie od wartości po przecinku.