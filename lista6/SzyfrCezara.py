ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(zdanie, klucz):
    encrypted = ""
    for i in zdanie:
        if(i in ascii_letters):
            char = i
            if(char.isupper()):
                encrypted += chr((ord(char) + klucz-65) % 26 + 65)
            else:
                encrypted += chr((ord(char) + klucz - 97) % 26 + 97)
        else:
            encrypted += i
    return encrypted

def decrypt(zdanie, klucz):
    decryption = ""
    for i in zdanie:
        if(i in ascii_letters):
            char = i
            if(char.isupper()):
                decryption += chr((ord(char) - klucz-65) % 26 + 65)
            else:
                decryption += chr((ord(char) - klucz - 97) % 26 + 97)
        else:
            decryption += i
    return decryption