#En python al trabajar con listas, es posible eliminar un elemento, especificando
# el elemento a eliminar, a diferencia del metodo pop(), donde tenemos que especificar la posicion exacta
# dentro de una lista, para eliminar el elemento.
#El metodo remove, permite eliminar un elemento dentro de una lista, especificando a traves de una argumento, el elemento que deseamos eliminar.#

vocales =["a","e","i","o","u"]
print(f"{vocales}\n elemento a eliminar i: ")
vocales.remove("i")
print(vocales)


vocales =["a","e","i","o","u"]
print(f"\n{vocales}\n elemento a eliminar o: ")
vocales.remove("o")
print(vocales)


vocales =["a","e","i","o","i"]
print(f"\n{vocales}\n elemento a eliminar i: ")
vocales.remove("i")
print(vocales)

vocales =["a","e","i","o","u"]
print(f"\n{vocales}\n elemento a eliminar I: ")
vocales.remove("I")
print(vocales)#sintax error example#
