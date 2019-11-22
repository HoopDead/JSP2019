import itertools

lista = [2,(17, -8),-11,(100, -100),6,"Ala", "Python",-4.0,"Ela",("Grzegorz Brzeczyszczykiewicz", "a", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")]

lista_number = []
lista_str = []

def rozdziel(arg):
    for x in arg:
        if type(x) == int or type(x) == float:
            lista_number.append(x)
        elif type(x) == str:
            lista_str.append(x)
        elif type(x) == tuple:
            for t in x:
                if type(t) == int or type(t) == float:
                    lista_number.append(t)
                elif type(t) == str:
                    lista_str.append(t)

    print("Najmniejsza liczba: ", min(lista_number))
    print("Najdłuższy łańcuch: ", max(lista_str, key = len))

rozdziel(lista)