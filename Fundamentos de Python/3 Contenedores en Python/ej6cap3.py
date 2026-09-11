#6. Crea un diccionario que contenga información sobre una película: 
# título, director y año. Luego:
#Accede al valor de cada clave con print().
#Agrega una nueva clave llamada género.
#Modifica el año.
#Elimina la clave director.

pelicula= {
    "titulo":"spiderman",
    "director":"Sam_Raimi",
    "año":2002
}

print(pelicula["titulo"])
print(pelicula["director"])
print(pelicula["año"])

pelicula["genero"]= "accion"

pelicula["año"] = 2025

del pelicula["director"]

print(pelicula)

