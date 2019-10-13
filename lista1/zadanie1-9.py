# Python code to demonstrate the working of 
# complex(), real() and imag() 
  
import numpy as np
import math 

x = input("Wprowadz wartosc rzeczywista: ")
y = input("Wprowadz wartosc urojona: ")

z = complex(int(x),int(y)); 
  
print ("Rzeczywista wartosc z liczby to: ") 
print (z.real) 
  
print ("Urojona czesc z liczby to: ") 
print (z.imag)

print(abs(z), " to wartosc bezwzgledna z liczby zespolonej")

print(np.conjugate(z))
