edad= int(input("Introduce tu edad por favor: "))

while edad<0:
    print("haz introducido una edad incorrecta.")
    edad= int(input("Introduce tu edad por favor: "))


print("Gracias por colaborar")
print("Edad del participante: " + str(edad))
