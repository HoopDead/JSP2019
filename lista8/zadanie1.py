import os
from datetime import date


ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dir_path = os.path.dirname(os.path.realpath(__file__))
print("Aktualnie jestes w: " + dir_path)
path = input("Wprowadz sciezke: ")
key = int(input("Wprowadz klucz do szyfrowania: "))


def FileCheck(path):
    try:
        f = open(path, "r")
        fileToString(path)
        return 1
    except IOError:
        print ("Blad: Plik nie istnieje! :o")
        return 0

def encryptFile(string, key):
    returnString = ""
    for i in string:
        if(i in ascii_letters):
            char = i
            if(char.isupper()):
                returnString += chr((ord(char) + key-65) % 26 + 65)
            else:
                returnString += chr((ord(char) + key - 97) % 26 + 97)
        else:
            returnString += i
    return returnString

def makeDir(encrypted):
    today = date.today()
    savePath = input("Wprowadz sciezke do zapisania: ")
    try:
        os.makedirs(savePath)
        os.chdir(savePath)
        fileName = 'plik_zaszyfrowany.txt{0}_{1}.txt'.format(key, today)
        f = open(fileName,"w+")
        f.write(encrypted)
        return 1
    except IOError:
        print("Podana sciezka juz istnieje!")


def fileToString(path):
    returnString = ""
    f = open(path, "r")
    f1 = f.readlines()
    for x in f1:
        returnString += x
    makeDir(encryptFile(returnString, key))
    
fileToString(path)
