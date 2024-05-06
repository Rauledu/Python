#Cuando se trabaja con listas, surge la necesidad de acceder a los elementos
# contenidos dentro de la misma, ya que de esta manera podemos consultar e incluso
# modificar su contenido. Para acceder a los elementos de una lista, es necesario
# apoyarnos de los indices, los cuales le indican a nuestro programa la posicion exacta
# del elemento con el cual deseamos trabajar dentro de una lista.#\

print("Accediendo a las posiciones de una lista")
marcas = ["Apple", "Samsumg", "Xiaomi", "Motorolla"]

print(f"\nLista completa: {marcas}")

print(f"\n Cuantos elementos tiene la lista? {len(marcas)}")

print(f"\nmarcas[1]: {marcas[1]}")

print(f"\nmarcas[3]: {marcas[3]}")

print(f"\nmarcas[-1]: {marcas[-1]}")

print(f"\nmarcas[-3]: {marcas[-3]}")

print(f"\nmarcas[1: 3]: {marcas[1: 3]}")

print(f"\nmarcas[: 2]: {marcas[: 2]}")

print(f"\nmarcas[1:]: {marcas[1:]}")

print(f"\nmarcas[:]: {marcas[:]}")

print(marcas)
