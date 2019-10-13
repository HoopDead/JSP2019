import cmath

z = 1j
print("Czesc rzeczywista z sinusa: ", cmath.sin(z.real))
print("Czesc urojona z sinusa: ", cmath.sin(z.imag))
print("Czesc rzeczywista z cosinusa:", cmath.cos(z.real))
print("Czesc urojona z cosinusa:", cmath.cos(z.imag))
print(cmath.cos(z) ** 2 + cmath.sin(z) ** 2, " - Warunek jest spełniony")