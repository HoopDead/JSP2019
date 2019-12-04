#Zadanie 1
a = {"a": 1, "b": 3, "c": 3, "d": 10, "e": 10, "f": 23, "g": 23, "h": 3, "aa": 2}
b = {}

def reduceDic(arg):
    for key, value in arg.items():
        if value not in b.values():
            b[key] = value
    return b

print(reduceDic(a))