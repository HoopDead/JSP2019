import operator

lista_1 = [20, 11,[5, -8],[1,-20],5,[-19,-8],-10,[7,-19],-15,[6,-12],[-17,9],2]

lista_1_temp = []
lista_2_temp = []



def sortuj(arg):
    l = len(arg)
    for i in range (0, l):
        if type(arg[i]) == int:
            lista_1_temp.append(abs(arg[i]))
        else:
            lista_2_temp.append((arg[i]))

    sorted_1 = sorted(lista_1_temp)
    sorted_2 = sorted(lista_2_temp, key=lambda x: x[0])
    print(sorted(lista_1_temp))
    print(sorted(lista_2_temp, key=lambda x: x[0]))
    print(sorted_1 + sorted_2)

print(sortuj(lista_1))
