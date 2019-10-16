napis = input("Wprowadz napis (NIECH LICZBA ZNAKOW BEDZIE PARZYSTA): ")

middle = len(napis) / 2

ans = napis[:int(middle)] + "Napisek" + napis[int(middle):]

print(ans)