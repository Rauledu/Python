#El metodo format(), nos permite mostrar los valores contenidos
# en una variable y utilizarlos dentro de una cadena de caracteres
# sustituyendo el nombre de la variable con un juego de {}, ubicandolas en la posicion
# donde queremos que se muestren dischos valores#

#1-alternativa

nombre = "Raul"
edad = 31
print ("Hola {} tienes {} años.".format(nombre, edad))

#2-alternativa

print ("Hola {nombre} tienes {edad} años".format(nombre="Raul", edad=31))


#3-alternativa

nombre = "Raul"
edad = 31

print ("Hola {1} tienes {0} años.".format(edad, nombre))
