m = int(input("Wprowadz wartosc m: "))
n = int(input("Wprowadz wartosc n: "))

arr = []
for i in range(m):
    arr.append([])
    for j in range(n):
        arr[i].append(i*j)

print(arr)