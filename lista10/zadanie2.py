class Sublist:
    def __init__(self, array):
        self.array = array

    def specify(self):
        specyfiyArray = [[]]

        for i in range(len(self.array) + 1):
            for j in range (i + 1, len(self.array) + 1):
                sub = self.array[i:j]
                specyfiyArray.append(sub)
        return specyfiyArray

def main():
    sublist = Sublist([1, 2, 3])
    print(sublist.specify())


if __name__ == "__main__":
    main()