print("calculadora con una sola variable \n")

print("*******************")
print("*Menu de opciones*")
print("*******************")

print("1.   suma")
print("2.   Resta")
print("3.   Multiplicación")
print("4.   Division")
print("5.   Division entera")
print("6.   Exponente")
print("7.   Modulo o resto \n")

numero = int(input("Introduce la opcion deseada:"))

if numero == 1:

    print("Elegistes suma \n")
    numero = int(input("Introduce el primer numero:"))
    numero += int(input("Introduce el segundo numero:"))
    print("El resultado de la suma es: ", numero)

elif numero ==2:

    print("Elegistes resta \n")
    numero = int(input("Introduce el primer numero:"))
    numero -= int(input("Introduce el segundo numero:"))
    print("El resultado de la resta es: ", numero)

elif numero ==3:

    print("Elegistes Multiplicacion \n")
    numero = int(input("Introduce el primer numero:"))
    numero *= int(input("Introduce el segundo numero:"))
    print("El resultado de la Multiplicacion es: ", numero)

elif numero ==4:

    print("Elegistes Division \n")
    numero = float(input("Introduce el primer numero:"))
    numero /= float(input("Introduce el segundo numero:"))
    print("El resultado de la Divison es: ", round(numero), 2)

elif numero ==5:

    print("Elegistes Division entera \n")
    numero = int(input("Introduce el primer numero:"))
    numero //= int(input("Introduce el segundo numero:"))
    print("El resultado de la Division entera es: ", numero)
    
elif numero ==6:

    print("Elegistes exponente \n")
    numero = int(input("Introduce el primer numero:"))
    numero **= int(input("Introduce el segundo numero:"))
    print("El resultado del exponente es: ", numero)
    
elif numero ==7:

    print("Elegistes modulo o resto \n")
    numero = int(input("Introduce el primer numero:"))
    numero %= int(input("Introduce el segundo numero:"))
    print("El modulo o resto es: ", numero)
else:
    print("La opcion elegida no existe.")



