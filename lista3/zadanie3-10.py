arr = []

i = 100

while (i <= 400):
    string = str(i)
    check = 0
    for j in range (3):
        if(int(string[j]) % 2 == 0):
            check = check + 1
    if(check == len(string)):
        arr.append(string)
    i =  i+1
    check = 0

print(arr)
