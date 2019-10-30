import colorsys

R = int(input("Wprowadz R: "))
G = int(input("Wprowadz G: "))
B = int(input("Wprowadz B: "))

R = R/255
G = G/255
B = B/255

lista = colorsys.rgb_to_hsv(R,G,B)
print(lista[0] * 360, lista[1], lista[2], sep = ", ")

