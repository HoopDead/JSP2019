import numpy

def obwod(a, b, c):
    return a+b+c

def pole(a, b, c):
    p = 0.5 * (a+b+c)
    return numpy.sqrt(p*(p-a)*(p-b)*(p-c))

def checkBoki(a,b,c):
    if(a == b) and (b == c) and (a==c):
        return "Trojkat równoboczny"
    elif (a==b) or (c==a) or (b==c):
        return "Trojkat równoramienny"
    else:
        return "Trójkat róznoboczny"

def checkTrojkat(a,b,c):
    if(a**2 + b**2 == c**2):
        return "Trojkat prostokatny"
    elif(a**2 + b**2 > c**2):
        return "Trójkat ostrokatny"
    else:
        return "Trójkat rozwartokatny"
