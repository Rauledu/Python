#En python, un diccionario es una esctructura de datos, que se utiliza para almacenar
# un conjunto de elementos no ordenados y al igual que las listas, un diccionario puede ser hmogeneo o heterogeneo.\
#Los diccionarios al igual que las listas, tienen la caracteristica de ser mutables, esto quiere decir
# que despues de haber sido creado su contenido se puede modificar.#

#Nota: KEY, es la clave para hacer referencia
# a un elemento dentro del diccionario.#

#Diccionario vacio
Dictionary_empty = {}

print(f"Diccinario vacio: {Dictionary_empty}")
print()

#Diccionario homogeneo
Dictionary_ages = {"Juan": 32, 
                    "Gerardo": 21, 
                    "Luis": 25
                                    }

print(f"Diccionario de edades: {Dictionary_ages}")
print()

#Diccionario heterogeneo
Dictionary_data = {"Name": "Brenda",
"Last name": "Florez",
"Age": 22
}

print(f"Diccionario de edades: {Dictionary_data}")
print()

#Un diccionario puede almacenar listas y diccionario.

Dictionary_list = {"a": {"a": 1},
"b": [0,1,2]
}

print(f"Diccionario con lista y diccionario: {Dictionary_list}")
print()

#Diccionario puede tener claves numericas
dictionary_keys_numn = {4: 1,
5: 2,
6:3
}
print(f"Diccionario con claves numericas: {dictionary_keys_numn}")
print()

#un diccionario no puede tener claves repetidas
dictionary_repeat_keys = {"Juan": 20,
"Gerardo": 30,
"Juan": 15
}
print(f"Diccionario con claves repetidas: {dictionary_repeat_keys}")
print()

#Un diccionario puede tener claves numericas o de tipo texto
Dictionary = {1: 32,
"Juan": 5,
-2: "Hola"}
print(f"Diccionario con claves de distintos tipos de datos: {Dictionary}")

