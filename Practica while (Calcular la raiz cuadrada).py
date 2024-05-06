import math

print ("Programa de calculo raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

Intentos=0

while numero<0:
    print("No se puede hallar la raiz.")

    if intentos ==2:
        print("haz consumido demasiados intentos. el programa ha finalizado.")
        break;
    numero=int(input("Introduce un numero por favor: "))
    if numero <0:
        intentos=intentos +1

if Intentos <2:
    solucion= math.sqrt(numero)
    print("La raiz cuadrada de  " + str(numero) + " es " + str(solucion))
