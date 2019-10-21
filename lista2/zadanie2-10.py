trojki = []

for i in range (33):
    trojki.append(3*i)

del trojki[4:33:3]

print(sum(trojki)/len(trojki))