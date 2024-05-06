#Las grandes ventajas al trabajar con listas, es que podemos modificar cada uno de sus elementos, de acuedo a nuestras necesidades.
# Modificar los elementos de una lista, es muy sencillo ya que la sintaxis que se utiliza, es similar a la sintaxis que utilzamos para acceder a los elementos de una lista.#

print("Modificando vocales[1]= 'x'")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[1]='x'
print(f"Lista vocales: {vocales}")

#---------------------------------------#
print("Modificando vocales[2]= '2'")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[1]= 2
print(f"Lista vocales: {vocales}")

#---------------------------------------#
print("Modificando vocales[-1]= 'x'")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[-1]='x'
print(f"Lista vocales: {vocales}")
#---------------------------------------#
print("Modificando vocales[2:4]= ['x', 'y']")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[2:4]=['x', 'y']
print(f"Lista vocales: {vocales}")

#-----------------------------------------#

print("Modificando vocales[1:3]= ['x', 'y']")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[1:3]=['x', 'y']
print(f"Lista vocales: {vocales}")

#------------------------------------------#

print("Modificando vocales[1:3]= ['x', 'y', 'z']")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[1:3]= ['x', 'y', 'z']
print(f"Lista vocales: {vocales}")

#------------------------------------------#

print("Modificando vocales[:2]= ['x', 'y', 'z']")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[:2]= ['x', 'y', 'z']
print(f"Lista vocales: {vocales}")

#------------------------------------------#

print("Modificando vocales[0:3]= ['x', 'y']")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[0:3]= ['x', 'y']
print(f"Lista vocales: {vocales}")

#-------------------------------------------#

print("Modificando vocales[0:3]= 'x', 'y'")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[0:3]= 'x', 'y'
print(f"Lista vocales: {vocales}")

#-------------------------------------------#
print("Modificando vocales[:]= 'x'")
vocales = ["a", "e", "i","o","u"]
print(f"\nLista vocales: {vocales}")
vocales[:]= 'x'
print(f"Lista vocales: {vocales}")
