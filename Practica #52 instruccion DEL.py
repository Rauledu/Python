#En python, al trabajar con listas, ademas de poder eliminar uno o varios elementos de una lista,
# es posible eliminar toda una lista para lograrlo
# contamos con la instruccion del, la cual nos permite
# eliminar toda una lista y a su vex nos permite eliminar un unico elemento indicando
# la posicion exacta del elemento.#

vocales =["a","e","i","o","u"]
print(f"Listas: {vocales}")
del vocales [3]
print(f"del vocales [1]: {vocales}")

vocales =["a","e","i","o","u"]
print(f"\nListas: {vocales}")
del vocales [0:2]
print(f"del vocales [0:2]: {vocales}")

vocales =["a","e","i","o","u"]
print(f"\nListas: {vocales}")
del vocales [:]
print(f"del vocales [:]: {vocales}")

vocales =["a","e","i","o","u"]
print(f"\nListas: {vocales}")
del vocales
print(f"del vocales: {vocales}")

