#Eliminacion de caracteres continuos#

Lista_original = ["A","B","b","D","e","F","g","c"]
print(f"Lista original: {Lista_original}")

elemento = input("Intrduce el elemento que deseas eliminar: ")

for _ in Lista_original:
    if elemento.lower() in Lista_original:
        Lista_original.remove(elemento.lower())
    elif elemento.upper() in Lista_original:
        Lista_original.remove(elemento.upper())

print(f"Elemento eliinado: {Lista_original}")

