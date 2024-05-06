#En python, podemos encontrarnos con la necesidad de tener un objeto iterable
# el cual queremos convertir a una lista y asi manipular cada uno de sus elementos.
#Una alternativa para convertir objetos iterables a listas, es utilizar un ciclo le cual se encargaria de recorrer
# cada uno de los elementos y a su vez ir almacenando uno a uno dentro de una lista. 
# Contamos con el constructor list(), el cual nos permite convertir objetos iterables a listas de una manera rapida
# compacta y eificente.#

print(range(0,100,10))

numeros = range(0,100,10)
print(numeros)
print( list(range(0,100,10)) )

nombre = "Raul"
print(list(nombre))

lista_nombres = list(nombre)
print(lista_nombres[::-1])