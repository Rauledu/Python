#Tabla de multiplicar#
num =int(input("Que tabla de multiplicar quieres ver?: "))
print ("la tabla es: {num}")

for i in range(11):
    print(f"{num} x {i} = {num * i}")
