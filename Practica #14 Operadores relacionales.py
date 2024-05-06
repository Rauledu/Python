#lo operadores relacionales son simbolos que se usan para comprarar dos valores y generalmente son utiizados en las sentencias condicionales para la#
#la toma de decisiones.#

print ("Introduce los numeros a comparar.\n")

num_uno = int(input("Introduce el primer numero:  "))
num_dos = int(input("Introduce el segundo numero:  "))

print("\n Los numeros a comparar son: ", num_uno, " y ", num_dos, "\n")

if num_uno == num_dos:
    print("Es igual...")
if num_uno != num_dos:
    print("Es diferente...")
if num_uno < num_dos:
    print("Es menor...")
if num_uno > num_dos:
    print("Es mayor...")
if num_uno <= num_dos:
    print("Es menor o igual...")
if num_uno >= num_dos:
    print("Es mayor o igual...")
print("Fin.")
