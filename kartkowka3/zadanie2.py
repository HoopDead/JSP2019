a = int(input("Wprowadz liczbe N: "))


back = a-1

for i in range(a+1):
    print("*" * i)

while back > 0:
    print("*" * back)
    back = back-1