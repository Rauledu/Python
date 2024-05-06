#los metodos istitle y title, los cuales se utilizan para identificar si la
# primera letra de cada palabra comienza con mayuscula, el resto de letras se encuentran en mminusculas
# de no ser asi, realiza la respectiva conversion #

Nombre = input("Nombre: ")
Apellido = input("Apellido: ")
full_name = f"{Nombre} {Apellido}"

print()
print (f"se ha aplicado el metodo title? {full_name.istitle()}")
print(f"Aplicando el metodo title():{full_name.title()}")