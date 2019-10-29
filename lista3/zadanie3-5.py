import re
password = input("Wprowadz swoje haslo: ")
petla = True
while petla:  
    if (len(password)<6 or len(password)>12):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[$#@]",password):
        break
    elif re.search("\s",password):
        break
    else:
        print("Ulozyles prawidlowe haslo.")
        petla=False
        break

if petla:
    print("Ulozyles nieprawidlowe haslo!")