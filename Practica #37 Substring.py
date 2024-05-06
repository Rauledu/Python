#En python, una cadena de caracteres, es una sucesion que puede contener caracteres
# especiales o alfanumericos.
# Es decir letras, numeros y/o simbolos.#

string = "0123456789"
substgring = ""

print (f"Cadena principal: {string}")

substgring = string [0]
print(f"\nsubcadena con indice en la posicion [0] es:{substgring}")

substgring = string [5]
print(f"\nsubcadena con indice en la posicion [5] es:{substgring}")

substgring = string [-4]
print(f"\nsubcadena con indice en la posicion [-4] es:{substgring}")

substgring = string [0:3]
print(f"\nsubcadena con indices en las posiciones [0:3] es:{substgring}")

substgring = string [:3]
print(f"\nsubcadena con indices en las posiciones [:3] es:{substgring}")

substgring = string [5:]
print(f"\nsubcadena con indices en las posiciones [5:] es:{substgring}")

substgring = string [-4:-1]
print(f"\nsubcadena con indices en las posiciones [-4:-1] es:{substgring}")

substgring = string [:]
print(f"\nsubcadena con indices en las posiciones [:] es:{substgring}")

substgring = string [1:6:2]
print(f"\nsubcadena con indices en las posiciones y salto [1:6:2] es:{substgring}")

substgring = string [::3]
print(f"\nsubcadena con indices en las posiciones y salto [::3] es:{substgring}")

