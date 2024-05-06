#En python es posible insertar elementos dentro de una lista, en una posicion determinda.
# Con lo cual, podremos establecer el orden y organizacion de todos los elementos que conformen a nuestras listas.
# A difencia del metodo append(), el metodo isnert() nos permite indicar la posicion exacta
# dentro de la lista, donde queremos agregar el nuevo elemento.#

print("Lista original:")
letters = ["b","d","f","g"]
print(f"Lista: {letters}")

print(f"\nInsertando 'a' en posicion 0: ")
letters.insert(0, "a")

print(f"Lista: {letters}")

print(f"\nInsertando 'c' en posicion 2: ")
letters.insert(2, "c")

print(f"Lista: {letters}")

print(f"\nInsertando 'e' en posicion 4: ")
letters.insert(4, "e")

print(f"Lista: {letters}")

print(f"\nInsertando 'z' en posicion 100: ")
letters.insert(100, "z")

print(f"Lista: {letters}")