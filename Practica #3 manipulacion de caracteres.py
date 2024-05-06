'Manipulacion de caracteres'

'Para asignacion +='
print("Asignacion:")
Mensaje = "Hola"
Mensaje += " "
Mensaje += 'Raúl'
print (Mensaje)

'Para concatenacion +'

print("Concatenacion:")
Variable = "Hola"
Variable2 = " "
Variable3 = "como estas?"
print(Variable + Variable2 + Variable3)

'Nota: al momento de realizar una concatenacion con un elemento int lo recomedable es usar un str para convertir dicho elemento en una variable de texto'
Valor1 = 4
Valor2 = 15
resultado =(Valor1 + Valor2)
resultado = str(resultado)
'se aplico la conversion del elemento int a texto'
print("El total de la suma es: " + resultado)

'para la busqueda find'
print("Busqueda:")
mensaje = "Hola mundo"
sub_cadena = mensaje.find("mundo")
print(sub_cadena)

'para extraer [:]'
print("extraccion:")
mensaje = "Hola Raúl"
extraccion = mensaje[1:8]
print(extraccion)

'para comparar =='
print("Comparar:")
mensaje = "hola"
mensaje2 = "Hola"
print(mensaje == mensaje2)



