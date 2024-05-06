#al trabajar co listas, se llega a la necesidad de agregar nuevos elementos a las
# mismas, para asi ampliar la cantidad de informacion con la que estamos trabajando.
# El metodo append() nos permite agregar nuevos elementos al final de una lista.#

print("Agregar un elemento a la lista: ")
letter = ["a","b","c","d"]
print(F"lISTA: {letter}")
letter.append("e")
print(f"Lista modificada:{letter}")


print("\nAgregar tres elementos a la lista: ")
letter = ["a","b","c","d"]
print(F"lISTA: {letter}")
letter.append("e")
letter.append("f")
letter.append("g")
print(f"Lista modificada:{letter}")

print("\nAgregando distinto tipo de dato a la lista: ")
letter = ["a","b","c","d"]
print(F"lISTA: {letter}")
letter.append("*")
letter.append(23)
letter.append("@")
print(f"Lista modificada:{letter}")