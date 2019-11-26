import SzyfrCezara as sc

string = input("Wprowadz zdanie: ")
klucz = int(input("Wprowadz klucz: "))

print("Zaszyfrowane: " + sc.encrypt(str(string), klucz))
encrypted = sc.encrypt(str(string), klucz)
print("Odszyfrowane: " + sc.decrypt(encrypted, klucz))