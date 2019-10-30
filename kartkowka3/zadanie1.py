#Zadanie 1

l = [0, 10, 8, 3, 5, 4, 7]
out = []

for i in range(len(l)):
    if (l[i] % 2 == 1):
        out.append(l[i])

print(out)