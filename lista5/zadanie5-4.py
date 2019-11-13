insert = input("Podaj zdanie: ")

key = {'a': 'y', 'e' : 'i', 'i' : 'o', 'o' : 'a', 'y': 'e'}

def szyfr(string, key):
    for item in string:
        if item in key.keys():
            string = string.replace(item, key[item])
    return string

def deszyfr(string, key):
    reverse_key = dict(map(reversed, key.items()))
    for item in string:
        if item in reverse_key.items():
            string = string.replace(item, reverse_key[item])
    return string

print(szyfr(insert, key))
print(deszyfr(insert, key))