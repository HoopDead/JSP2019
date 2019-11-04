ilosc = int(input("Wprowadz ilosc n: "))

sum = 1

for i in range (1, ilosc + 1):
    sum *= i

print("Silnia z ", ilosc, " to: ", sum)
