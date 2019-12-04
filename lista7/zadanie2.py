import random

A = []
    
def insertion_sort(arg): 
    for i in range(1, len(arg)):
        key = arg[i]  
        j = i-1
        while j >=0 and arg[j] > key: 
            arg[j+1] = arg[j] 
            j -= 1
        arg[j+1] = key 
    return arg


def main(dlugosc):
    for i in range (dlugosc):
        A.append(random.randint(1, 20))
    return A

main(100)
print(insertion_sort(A))