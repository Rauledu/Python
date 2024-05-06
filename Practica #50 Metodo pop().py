#al trabajar con listas, ademas de agregar y acceder a elementos, es posible eliminar elementos de una lista, ya sea el ultimo elemento o bien un elemento
# en especifico.
# para eliminar elementos de una lista contamos con el metodo pop(), el cual nos permite acceder a la lista y eliminar
# ya sea el ultimo elemento o bien un elemento en especifico
# para lo cual se debe especificar su posicion exacta dentro de la lista.#

vocales =["a","e","i","o","u"]
print(f"Lista original: {vocales}")
print(f"elemento eliminado: {vocales.pop()}")
print(f"lista: {vocales}")

vocales =["a","e","i","o","u"]
print(f"\nLista original: {vocales}")
print(f"elemento eliminado en la posicion 2: {vocales.pop(2)}")
print(f"lista: {vocales}")

vocales =["a","e","i","o","u"]
print(f"\nLista original: {vocales}")
print(f"elemento eliminado en la posicion 0: {vocales.pop(0)}")
print(f"lista: {vocales}")

vocales =["a","e","i","o","u"]
print(f"\nLista original: {vocales}")
print(f"elemento eliminado en la posicion -2: {vocales.pop(-2)}")
print(f"lista: {vocales}")

vocales =["a","e","i","o","u"]
print(f"\nLista original: {vocales}")
print(f"elemento eliminado en la posicion 5: {vocales.pop(5)}")
print(f"lista: {vocales}") #Este es un ejemplo de error#