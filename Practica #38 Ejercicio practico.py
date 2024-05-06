Oracion = input("introduce una Oracion: ")
Question = input("Que palabra desea eliminar?: ")
substring = ""
indice = Oracion.find(Question)
substring = Oracion[0:indice] + Oracion[indice + len(Question) +1 : ]

print(f"Cadena resultante: {substring}")


