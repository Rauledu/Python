'Practica condicional simple'
print ("Sistema para calcular el promedio de un alumno.")

Nombre = input("Para iniciar, ¿cual es tu nombre?: ")

Matematicas = int(input(Nombre + " ¿Cual es tu calificación en matematicas?: "))
Quimica = int(input(Nombre + " ¿Cual es tu calificación en quimica?: "))
Fisica = int(input(Nombre + " ¿Cual es tu calificación en fisica?: "))

Promedio = (Matematicas + Quimica + Fisica) / 3
'Promedio = int(Promedio)'

if Promedio >=6:
    print('feliciades '+ Nombre +' "apobastes" con un promedio de: ', Promedio)

print("Fin.")
