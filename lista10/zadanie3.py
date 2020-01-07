class Triple:
    def __init__(self, array):
        self.array = array

    def findTriple(self):
        found = False
        for i in range(len(self.array) - 1): 
            s = list() 
            for j in range(i + 1, len(self.array)): 
                x = -(self.array[i] + self.array[j]) 
                if x in s:
                    s.append(x)
                    s.append(self.array[i])
                    s.append(self.array[j])
                    found = True
                else: 
                    s.append(x)
                    s.append(self.array[i])
                    s.append(self.array[j])
                return s
        if found == False: 
            print("No Triplet Found") 

def main():
    array = Triple([1, 2, -3])
    print(array.findTriple())

if __name__ == "__main__":
    main()