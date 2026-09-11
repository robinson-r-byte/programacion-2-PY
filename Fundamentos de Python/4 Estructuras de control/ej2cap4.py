#2. Escribe un programa que solicite la edad del usuario y muestre 
#-un mensaje personalizado según su rango:
#-Menor de 12: “Eres un niño”.
#-Entre 12 y 17: “Eres un adolescente”.
#-Entre 18 y 59: “Eres un adulto”.
#-60 o más: “Eres un adulto mayor”

edad = int(input("INGRESA LA EDAD:"))

if edad >= 60:
    print("Eres un adulto mayor")
elif edad >= 18:
    print("Eres un adulto")
elif edad >= 12:
    print("Eres un adolescente")
else:
    print("Eres un niño")    
        