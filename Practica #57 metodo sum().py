#el metodo sum(), permite regresar la suma de todos los elementos de una lista, compuesta unicamente
# por valores numericos.#

nuumeros = [1,2,3]
print(nuumeros)
print(sum(nuumeros))

nuumeros = [1,2,3]
print(f"\nCon valor inicial 10 \n{nuumeros}")
print(sum(nuumeros,10))

nuumeros = [1,2,3]
print(f"\nCon valor inicial -2 \n{nuumeros}")
print(sum(nuumeros,-2))

nuumeros = [1,2,3,True]
print(f"\nLista \n{nuumeros}")
print(sum(nuumeros))