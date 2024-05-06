print("************************************************************************")
print("*programa para determinar ¿cual es el numero mas grande de tres numero?*")
print("************************************************************************\n")

numero_uno = int(input("Introduce el primer número: "))
numero_dos = int(input("Introduce el segundo número: "))
numero_tres = int(input("Introduce el tercer número: "))


if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El numero", numero_uno, " es el numero mas grande de los tres.")
else:
    if numero_dos > numero_tres:
        print("El numero", numero_dos, " es el numero mas grande de los tres.")
    else:
        print("El numero", numero_tres, " es el numero mas grande de los tres.")

print("Fin...")


