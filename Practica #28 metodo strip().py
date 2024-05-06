#Se utiliza para eliminar caracteres
# especificados al inicio y al final de una cadena
# de caracteres, tomando en cuena que si al metodo
# strip no se le especifica uno o mas caracteres
# a eliminar, solo elimina espacios en blanco y saltos
# de linea.#

cadena = "\tHola Raul\n"
print (cadena)

cadena = cadena.strip("H Rul\t\n")
print(cadena)