#la sentencia break se utiliza para detener la ejecucion de una iteracion y salir de ella,#
#con lo cual, el programa podra continuar con la ejecucion del codigo que se encuentre fuera de nuestro bucle.#

#Break#
print("while con la sentencia break \n")
contador = 0
while contador < 10:
    contador  += 1

    if contador == 5:
        break

    print("Valor actual de la variable: ", contador)

print("fin del proceso, la sentencia break ha sido ejecutada. \n")

#la sentencia continue permite detener la iteracion actual y volver al principio del#
#bucle para realizar una nueva iteracion, si es que la condicion que rife a nuestro bucle
#se sigue cumpliendo#

#Continue#

print("while con la sentencia continue \n")
contador = 0
while contador < 10:
    contador  += 1

    if contador == 5:
        continue

    print("Valor actual de la variable: ", contador)
