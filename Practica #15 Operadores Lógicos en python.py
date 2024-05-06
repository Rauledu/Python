#los operadores logicos permiten agrupar condicones dentro de una misma condición. Ess decir, con los operadores logicos tenemos la posibilidad de utilizar multiples operadores#
#relacionales dentro de una misma condición lógica.#

#Conjunción#
print("Cojunción (and)")

num_uno = int(input("Escribe un numero mayor a 2 y menor a 5:"))

if num_uno > 2 and num_uno < 5:
    print("El numero ", num_uno, " cumple con la condicion.\n")
else:
    print("El numero ", num_uno, " No cumple con la condicion-\n")

#Disyuncion#
print("Disyunción (or)")

palabra = input("Para cumplir con la condicon escribe 'Si' o 'yes':")

if palabra == "Si" or palabra == "yes":
    print("La condicion se ha cumplido.\n")
else:
    print("La condicion no se cumplido.\n")


#Negación#
print("Negación (not)")
    
num_uno = int(input("Introduce un numero igual a 5: "))

if not num_uno == 5:
    print("\n El numero es diferente de cinco y si cumple la condición.\n")
else:
    print("\n El numero es igual a cinco y no cumple la condición.\n")
