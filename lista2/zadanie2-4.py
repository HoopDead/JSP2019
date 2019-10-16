napis = input("Wprowadz napis")

first_letter = napis[0]

napis = napis.replace(napis[0], '$')

ans = first_letter + napis[1:]

print(ans)
    