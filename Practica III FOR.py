valido = False

email=input("Introduce tu email: ")

for i in range(len(email)):

    if email[i]=="@":
        valido=True

if valido:
    print("El correo es correcto.")
else:
    print("El correo es incorrecto.")
