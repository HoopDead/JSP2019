import re

insert = str(input("Wprowadz liczbe: "))

def word2int(arg):
    

liczby = {
    'zero': 0,
    'jeden': 1,
    'dwa': 2,
    'trzy': 3,
    'cztery': 4,
    'piec': 5,
    'szesc': 6,
    'siedem': 7,
    'osiem': 8,
    'dziewiec': 9,
    'dziesiec': 10,
    'jedenascie': 11,
    'dwanascie': 12,
    'trzynascie:' 13,
    'czternascie': 14,
    'pietnascie': 15,
    'szesnascie': 16,
    'siedemnascie': 17,
    'osiemnascie': 18,
    'dziewietnascie': 19
}

print(int(insert))

#assert funkcja("jeden") == 1
#assert funkcja("trzydziesci trzy") == 33
#assert funkcja ("trzynascie") == 13
#http://code.activestate.com/recipes/578258-spoken-word-to-number/