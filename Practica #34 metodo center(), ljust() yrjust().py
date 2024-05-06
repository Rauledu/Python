#Metodo center: nos permite centrar un string,añadiendo espacios o caracteres segun nosotros
# lo indiquemos, tanto al inicio y al final del string, para posteriormente mostrarnos el mismo string, pero
# con los cambios realizados.#

#center#

string = "menu"
print(string.center(20, "="))


#ljust(), nos permite alinear un string a la izquiera, anadiendo espacios o caracteres segun nostros los indiquemos
# unicamente al final del string, para posteriormente mostrarnos el mismo string pero con los cambios
# realizados.#

#ljust#

string = "menu"
print(string.ljust(20, "="))

#rjust(), nos permite alinear un string a la derecha, anadiendo espacios o caracteres segund
# nosotros lo indiquemos, unicamente al inicio del string para posteriormente mostranos el mismo string
# pero con los cambios realizados.#

#rjust#

string = "menu"
print(string.rjust(20,"="))

#variable modificada#

print(f"Variable modificada")
string  = string.center(10, "+")
print(string)