#el metodo count es de gran utilidad cuando tenemos la necesidad de conocer
# la cantidad de veces que aparece una cadena o caracter en especifico dentro de un texto.#

string = "MI MAMA ME MIMA"
contador = 0
print(string.center(40 , "="))

contador = string.count("m")
print(f"\n la letra m se encontro {contador} veces en la cadena: {string}")


contador = string.count("MAMA")
print(f"\n la letra MAMA se encontro {contador} veces en la cadena: {string}")

contador = string.count("ME MIMA")
print(f"\n la letra ME MIMA se encontro {contador} veces en la cadena: {string}")

contador = string.count("Ma")
print(f"\n la letra Ma se encontro {contador} veces en la cadena: {string}")

contador = string.count("m", 13)
print(f"\n la letra m se encontro {contador} veces, desde la posicion 13 en la cadena: {string}")

contador = string.count("m", 100)
print(f"\n la letra m se encontro {contador} veces, desde la posicion 100 en la cadena: {string}")

contador = string.count("m", -3)
print(f"\n la letra m se encontro {contador} veces, desde la posicion -3 en la cadena: {string}")

contador = string.count("m", 3, 7)
print(f"\n la letra m se encontro {contador} veces, desde la posicion 3 hasta la posicion 7 en la cadena: {string}")

contador = string.count("m", 100, 100)
print(f"\n la letra m se encontro {contador} veces, desde la posicion 100 hasta la posicion 100 en la cadena: {string}")

contador = string.count("m", -4, -1)
print(f"\n la letra m se encontro {contador} veces, desde la posicion -4 hasta la posicion -1 en la cadena: {string}")




