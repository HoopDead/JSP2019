import numpy as np

class Kolo:
    def __init__(self, radius):
        self.radius = radius

    def obwod(self):
        return 2 * np.pi * self.radius

    def pole(self):
        return np.pi * self.radius**2

def main():
    kolko = Kolo(5)
    print(f"Obwód: {kolko.obwod()}")
    print(f"Pole: {kolko.pole()}")

if __name__ == "__main__":
    main()