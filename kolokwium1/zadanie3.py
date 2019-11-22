def anagram(arg):
    result = ""
    for i in arg:
        result = arg[::-1]
    if(arg == result):
        return ("Podane słowo '" + arg + "' jest anagramem, poniewaz równa się: '" + result + "'")
    else:
        return ("Podane słowo '" + arg + "' nie jest anagramem, poniewaz nie równa się: '" + result + "'")

slowo = input("Wprowadz slowo: ")

print(anagram(slowo))