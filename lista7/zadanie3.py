import random

A = []

def bubble_sort(arg):
    n = len(arg)
    i = 0
    while(n>1):
        while(i < n-1):
            if(arg[i] > arg[i+1]):
                temp = arg[i]
                temp2 = arg[i+1]
                arg[i] = temp2
                arg[i+1] = temp
            i = i+1
        n = n-1
        i = 0
    return arg


def main(dlugosc):
    for i in range(dlugosc):
        A.append(random.randint(1,20))
    return A

main(100)
print(bubble_sort(A))