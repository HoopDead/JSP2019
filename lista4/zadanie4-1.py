a = [1, 2, 3, 4, 5, 20]

suma = 0
iloczyn = 1

for i in range (len(a)):
    suma += a[i]
    iloczyn *= a[i]

print("Suma: ", suma)
print("Iloczyn: ", iloczyn)