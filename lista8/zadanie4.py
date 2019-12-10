import os
import datetime


def calc_check_digit(number):
    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    check = sum(w * int(n) for w, n in zip(weights, number))
    if str((10 - check) % 10) == number[10]:
        return 1
    else:
        return 0


def get_birth_date(number):
    year = int(number[0:2])
    month = int(number[2:4])
    day = int(number[4:6])
    year += {
        0: 1900,
        1: 2000,
        2: 2100,
        3: 2200,
        4: 1800,
    }[month // 20]
    month = month % 20
    try:
        return datetime.date(year, month, day)
    except ValueError:
        raise InvalidComponent()

def get_gender(number):
    if number[9] in '02468':  # even
        return 'F'
    else:  # odd: 13579
        return 'M'

def checkPesel(string):
    for x in range (len(string)):
        print (x)

def fileCheck():
    try:
        f = open("PESEL.TXT", "r")
        fileToString("PESEL.TXT")
        return 1
    except IOError:
        print ("Blad: Plik nie istnieje! :o")
        return 0

def makeDir(value):
    f = open("PESELDESZYFR.txt","w+")
    f.write(value)

def fileToString(path):
    zero = 0
    last = 11
    value = ""
    returnString = ""
    f = open(path, "r")
    f1 = f.readlines()
    for x in f1:
        returnString += x
    for x in range (10):
        if(calc_check_digit(returnString[zero:last]) == 1):
            dataUr = str((get_birth_date(returnString[zero:last])))
            gender = (get_gender(returnString[zero:last]))
            value += returnString[zero:last] + " " + gender + " " + dataUr + '\n'
            makeDir(value)
        # print(zero, last)
        zero += 12
        last += 12

fileCheck()