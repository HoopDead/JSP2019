ilosc = int(input("Wprowadz ilosc elementow: "))

sum = 0

for i in range (1, ilosc+1):
    print(i)
    sum += 1/i

print("Suma elementow  ", ilosc, " to: ", sum)