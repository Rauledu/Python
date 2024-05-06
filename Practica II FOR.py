contador = 0
miEmail=input("introduce tu direccion de email: ")

for i in miEmail:

    if(i=="@" or i=="."):
        
        contador +=1
        
if (contador == 2):
    print("Email es correcto")
else:
    print("El email es incorrecto")



for i in range(5,50,3):
    print("valor de la variable :" , i )
