def num2words(num):
    under_20 = ['zero','jeden','dwa','trzy','cztery','piec','szesc','siedem','osiem','dziewiec','dziesiec','jedenascie','dwanascie','trzynascie','czternascie','pietnascie','szesnascie','siedemnascie','osiemnascie','dziewietnascie']
    tens = ['', '', 'dwadziescia','trzydziesci','czterdziesci','piecdziesiat','szescdziesiat','siedemdziesiat','osiemdziesiat','dziewiecdziesiat']
    setki = ['', 'sto', 'dwiescie', 'trzysta', 'czterysta', 'piecset', 'szescset', 'siedemset', 'osiemset', 'dziewiecset']
    tysiace = ['tysiac']
 
    if num < 20:
        return under_20[num]

    if num < 100:
        arr = ([int (i) for i in str(num)])
        return tens[arr[0]] + " " + under_20[arr[1]]

    if (num > 99) and (num < 1000):
        arr = ([int (i) for i in str(num)])
        return setki[arr[0]] + " " + tens[arr[1]] + " " + under_20[arr[2]]

    if(num > 999):
        arr = ([int (i) for i in str(num)])
        check = str(arr[2]) + str(arr[3])
        if(int(check) > 10) and (int(check) < 20):
            return tysiace[0] + " " + setki[arr[1]] + " " + under_20[int(check)]
        else:
            return tysiace[0] + " " + setki[arr[1]] + " " + tens[arr[2]] + " " + under_20[arr[3]]

print(num2words(1538))
assert num2words(1511) == "tysiac piecset jedenascie"
assert num2words(698) == "szescet dziewiedziesiat osiem"
