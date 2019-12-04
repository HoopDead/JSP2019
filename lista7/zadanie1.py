#Iteracyjnie

a = int(input("Wprowadz liczbe: "))

def fibonacci_iteracyjnie(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Zla liczba")
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
            print(c)
        return c


#Rekurencyjnie
def Fibonacci_rekurencyjnie(n):
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci_rekurencyjnie(n-1)+Fibonacci_rekurencyjnie(n-2) 
    
    
print("Iteracyjnie: " + str(fibonacci_iteracyjnie(a)))
print("Rekurencyjnie: " + str(Fibonacci_rekurencyjnie(a+1)))