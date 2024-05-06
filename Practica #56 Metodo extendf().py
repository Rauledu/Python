#Una de las tareas mas habituales al trabajar con listas, es concatenarlas es decir unir dos o mas listas para formar una lista unica.
# Existen multiples alternativas para concatenar dos o mas listas, entre las que destaca el metodo extend(),
#permite concatenar dos o mas listas y asu vez nos permite agregar varios elementos a una lista, como elementos individuales a partir de una secuencia.

Invitados = ["Raul","Xiomara","Andrea"]
conocidos = ["Gerardo","Miguel"]
print(f"Lista invitados: {Invitados} \nlista amigos: {conocidos}")
Invitados.extend(conocidos)
print(f"Lista invitados: {Invitados}")

numero= [10,20]
print(f"\n lista nuumeros: {numero}")
numero.extend( range(30,100,10))
print(f"Lista numeros: {numero}")

# Esto es una prueba para la practica Git.