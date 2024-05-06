#Al trabaar con listas, cuando se ingresan los elementos que formaran parte de la misma,
# no siempre son ingresados de manera ordenada, con lo cual nuestras listas pueden carecer de un orden en la informacion que contienen.
# Para esta situacion contamos con el metodo sort(), que permite ordenar una lista, tanto en orden ascendente o descendente, dependiendo de nuestras necesidades.

numeros = ["5","2","1","3","4"]
vocales= ["e","a","i","u","o"]

print(f"Lista de numeros: {numeros}")
numeros.sort()
print(f"\n Lista de numeros: {numeros}")
numeros.sort(reverse=True)
print(f"\n Lista de numeros: {numeros}")

#-----------------------------------------#
print(f"\n Lista vocales: {vocales}")
vocales.sort()
print(f"\n Lista vocales: {vocales}")
vocales.sort(reverse=True)
print(f"\n Lista vocales: {vocales}")
