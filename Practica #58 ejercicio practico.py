#Manejo de listas.#

numeros = []
longitud_lista = int(input("cuantos numeros enteros obtendra una lista: "))

for _ in range(longitud_lista):
    numeros.append(int(input("Introduce el numero entero: ")))

print(f"\n Lista: {numeros} \nLa suma total de los elementos es: {sum(numeros)}")