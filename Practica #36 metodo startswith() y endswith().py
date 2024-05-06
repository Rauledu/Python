#El metodo startswith(), se utiliza para comprobar si una cadena de caracteres
# comienza con una subcadena en particular.

#El metodo Endswith(), se utiliza para comprobar si una cadena de caracteres
# termina con una subcadena en particular.

# Ademas, es posible establecer un rango de busqueda dentro de la cadena principal.#

string = "Diana se peina sola"
resultado = 0
starts_with = "Ejemplo con startswith"
end_with = "Ejemplo con endswith"
print(f"\n{starts_with.rjust(50, '=')}")

resultado = string.startswith("D")
print(f"\n {string} comienza con la subcadena D: {resultado}")


resultado = string.startswith("d")
print(f"\n {string} comienza con la subcadena d: {resultado}")

resultado = string.startswith("Diana")
print(f"\n {string} comienza con la subcadena Diana: {resultado}")

resultado = string.startswith("se", 6)
print(f"\n {string} comienza con la subcadena se, desde la posicion 6: {resultado}")

resultado = string.startswith("se", 6, 7)
print(f"\n {string} comienza con la subcadena se, desde la posicion 6 hasta la posicion 7: {resultado}")

resultado = string.startswith("se", 100, 100)
print(f"\n {string} comienza con la subcadena se, desde la posicion 100 hasta la posicion 100: {resultado}")

resultado = string.startswith("se", -4, -1)
print(f"\n {string} comienza con la subcadena se, desde la posicion -4 hasta la posicion -1: {resultado}")


print(f"\n{end_with.rjust(50, '=')}")

resultado = string.endswith("A")
print(f"\n {string} termina con la subcadena A: {resultado}")

resultado = string.endswith("a")
print(f"\n {string} termina con la subcadena a: {resultado}")

resultado = string.endswith("sola")
print(f"\n {string} termina con la subcadena sola: {resultado}")

resultado = string.endswith("sola", 10)
print(f"\n {string} termina con la subcadena sola, desde la posicion 10: {resultado}")

resultado = string.endswith("s", 9, 14)
print(f"\n {string} termina con la subcadena s, desde la posicion 9 hsata la posicion 14: {resultado}")

resultado = string.endswith("s", 100, 100)
print(f"\n {string} termina con la subcadena s, desde la posicion 100 hsata la posicion 100: {resultado}")

resultado = string.endswith("s", -2, -4)
print(f"\n {string} termina con la subcadena s, desde la posicion -2 hsata la posicion -4: {resultado}")

