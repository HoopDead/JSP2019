wiersze = int(input("Wprowadz ilosc n: "))

arr = []

for wiersz in range(1, wiersze + 1):
    arr.append(1)
    for i in range(wiersz - 2, 0, -1):
        arr[i] += arr[i-1]

    print("Wiersz", wiersz, arr)