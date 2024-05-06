#Crear una mtriz por teclado.#

row = int(input("Cuantas filas tendra la matriz?: "))
Colums = int(input("Cuantas columnas tendra la matriz?: "))
matrix =[]

for row_position in range(row):
    row = []
    for element in range(Colums):
        row.append(int(input(f"Introduce un elemento a la fila {row_position}: ")))
    matrix.append(row)

for row in matrix:
    print(row)
