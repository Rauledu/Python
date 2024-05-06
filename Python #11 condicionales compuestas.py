'Practica condicional simple'
print ("Sistema para calcular el promedio de un alumno.")

Nombre = input("Para iniciar, ¿cual es tu nombre?: ")

Matematicas = float(input(Nombre + " ¿Cual es tu calificación en matematicas?: "))
Quimica = float(input(Nombre + " ¿Cual es tu calificación en quimica?: "))
Fisica = float(input(Nombre + " ¿Cual es tu calificación en fisica?: "))

Promedio = (Matematicas + Quimica + Fisica) / 3
'Promedio = int(Promedio)'

if Promedio >=6:
    print('felicidades '+ Nombre +' "aprobastes" con un promedio de: ', Promedio)
    print('felicidades '+ Nombre +' "aprobastes" con un promedio de: ', round(Promedio, 2))
    'el round lo utilizamos para valores flotantes e indicar la cantidad de decimales que queremos ver en pantalla'
                                                                                                
else:
    print("Lo sentimos " + Nombre + " has 'reprobado' con un promedio de: ", Promedio)
    print("Lo sentimos " + Nombre + " has 'reprobado' con un promedio de: ", round(Promedio, 2))

print("Fin.")
