x = list(input("Wprowadz liczbe elementow: "))

def usun(arg):
    arg = list(set(x))
    print(arg)

usun(x)