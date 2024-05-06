#String sin vocales#
string = input("INtroduce una frase: ")
Letter = input("Con que frase deseas terminar el bucle?: ")

for Char in string:
    if Char.lower() ==Letter.lower():
        break
    elif Char.lower() =="a":
        continue
    elif Char.lower() =="e":
        continue
    elif Char.lower() =="i":
        continue
    elif Char.lower() =="o":
        continue
    elif Char.lower() =="u":
        continue
    print(Char, end="")