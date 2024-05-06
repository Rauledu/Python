#los metodos islower y lower, se utilizan para identificar
# si todas las letras de una cadena de caracteres se enceuntran
# en minisculas y de no ser asi, convertir todas las letras en minisculas.#

# los metodos isupper y upper, se utilizan para identificar si todas las letras de una cadena de caracteres
# se encuentran en mayusculas y de no ser asi, convertir todas las letras en minisculas.#

#Metodo lower, islower#
string = input("Por favor introduce un string: ")
print(f"\nTodas las letras estan en minusculas?:{string.islower()}")
string = string.lower()
print(f"string en minusculas: {string}")

print(f"\nTodas las letras estan en mayusculas? {string.isupper()}")
print(f"string en mayusculas:{string.upper()}")
print(f"string original: {string}")