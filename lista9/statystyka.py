import sys
import numpy as np



def getSys(arg):
    b = list()
    b = [int(x) for x in arg.split(',')]
    return b

def getFile(arg):
    b = list()
    with open(arg) as filename:
        for line in filename:
            line = line.replace("\r\n", "")
            b.append(int(line))
    return b

def countData(arg):
    print(np.average(arg))
    print(np.var(arg))
    print(np.std(arg))

if ".txt" in sys.argv[1]:
    countData(getFile(sys.argv[1]))
else:
    countData(getSys(sys.argv[1]))
