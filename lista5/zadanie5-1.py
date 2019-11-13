import re

insert = str(input("Wprowadz liczbe: "))

def word2int(arg):
    liczby = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec", "dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
    argSplit = arg.split()
    if ("dziescia" in argSplit[0]):
        replaceVal = argSplit[0].replace('dziescia', '')
        returnVal = replaceVal
        returnVal = str(liczby.index(returnVal)) + str(liczby.index(argSplit[1]))
        return int(returnVal)
    elif("dziesci" in argSplit[0]):
        replaceVal = argSplit[0].replace('dziesci', '')
        if(replaceVal == "czter"):
            replaceVal = "cztery"

        returnVal = replaceVal
        returnVal = str(liczby.index(returnVal)) + str(liczby.index(argSplit[1]))
        return int(returnVal)
        return returnVal
    elif("dziesiat" in argSplit[0]):
        replaceVal = argSplit[0].replace('dziesiat', '')
        returnVal = replaceVal
        returnVal = str(liczby.index(returnVal)) + str(liczby.index(argSplit[1]))
        return int(returnVal)
        return returnVal
    elif(len(argSplit) == 1):
        return (liczby.index(argSplit[0]))
    elif(len(argSplit) == 2):
        returnVal = (liczby.index(argSplit[0]) + liczby.index(argSplit[1]))
        return returnVal

print(word2int(insert))

assert word2int("jeden") == 1
assert word2int("trzydziesci trzy") == 33
assert word2int ("trzynascie") == 13
#http://code.activestate.com/recipes/578258-spoken-word-to-number/