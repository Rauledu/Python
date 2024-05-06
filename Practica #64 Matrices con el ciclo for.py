#Al trabajar con matrices, es necesario tener acceso a cada uno de sus elementos de manera automatizada, ya que de esta  manera podemos manipular y trabajr
# con la informacion contenida dentro de las matrices.
# para esta situacion, podemos apoyarnos del ciclo for el cual nos permitira automatizar el acceso a la informacion
# contenida dentro de cada fila y columna de una matriz.#

matrix = [  [1,2,3],
            [4,5,6],
            [7,8,9] ]

print("Mostrar todo los elementos de la matriz fila por fila")
for row in matrix:
    print(row)

print("Mostrar todo los elementos de la matriz elemento por elemento")
for row in matrix:
    for element in row:
        print(element)

print("Mostrar todo los elementos de la matriz en formato de matriz")
for row in matrix:
    for element in row:
        print(element, end= " " )
    print()

