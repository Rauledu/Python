#En python al trabajar con los elementos que conforman una lista,
# surge la necesidad de buscar un elemento especifico para eliminarlo
# o bien para manipularlo de acuerdo a nuestras necesidades.
#se cuenta con el metodo index(), el cual permite localizar dentro de una lista, un elemento especifico.
#El metodo index(), devuelve un valor de tipo entero, el cual representa
# el indice de la primera coincidencia del elemento especificado a encontrar.#
#Este medoto, nos permite trabajar con minimo un argumento y maximo tres argumentos de manera 
# simultanea.#

vocales =["a","e","i","o","u","a"]
print(f"Lista: {vocales}")
print(f"La letra a que esta en la posicion: {vocales.index('a')}")
print(f"La letra i que esta en la posicion: {vocales.index('i')}")
print(f"La letra u en el rango 2-final que esta en la posicion: {vocales.index('u', 2)}")
print(f"La letra i en el rango 2-4 que esta en la posicion: {vocales.index('i', 2, 4)}")
