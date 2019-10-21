studenci = ["Kasia", "Basia", "Darek"]

studenci.append("Józek")

studenci.extend(["Ania", "Basia"])

studenci.sort()

print("Czwarty student: ", studenci[3], "Dwóch pierwszych: ", studenci[0:2], "Dwóch ostatnich: ", studenci[len(studenci)-2:])

studenci = list(dict.fromkeys(studenci))
studenci.remove("Basia")

dlugosc = len(studenci)

studenci = tuple(studenci)
