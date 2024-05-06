'las sentencias condicionales anidadas se presentan cuando por el camino de verdadero o falso de una sentencia condicional, hay otra sentencia condicional.'

print("=========")
print("Conversor")
print("========= \n")
print ("Menú de opciones: \n")
print("Presiona 1 para convertir a numero.")
print("Presiona 2 para convertir a palabra.\n")
Opcion = int(input("escribe la opcion deseada:"))
if Opcion == 1:
    print("\n Conversor de numero a palabra.\n")
    Opcion_uno = int(input("¿Cual es el numero que deseas convertir a palabra?: "))
    if Opcion_uno == 1:
        print("El numero es 'Uno'")
    elif Opcion_uno == 2:
        print("El numero es 'Dos'")
    elif Opcion_uno == 3:
        print("El numero es 'Tres'")
    elif Opcion_uno == 4:
        print("El numero es 'Cuatro'")
    elif Opcion_uno == 5:
        print("El numero es 'Cinco'")
    else:
        print("El numero no esta registrado.")
elif Opcion == 2:
    print("\n Conversor de palabra a numero.\n")
    Opcion_dos = input("¿Cual es la palabra que deseas convertir a numero?: ")
    Opcion_dos = Opcion_dos.lower()#la propiedad lower() permite convertir cualquier cadena de caracteres en minuscula.#
    if Opcion_dos == "uno":
        print("El numero es '1'")
    elif Opcion_dos == "dos":
        print("El numero es '2'")
    elif Opcion_dos == "tres":
        print("El numero es '3'")
    elif Opcion_dos == "cuatro":
        print("El numero es '4'")
    elif Opcion_dos == "cinco":
        print("El numero es '5'")
    else:
        print("El numero no esta registrado.")
else:
    print("Opcion no disponible.")

print("Fin.")

