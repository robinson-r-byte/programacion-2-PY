#6. Crea un ciclo while que sume números ingresados por el usuario. El programa debe
#terminar cuando el usuario escriba “salir”. Al final, muestra la suma total

suma = 0

while True:
    numero = (input("Ingresa un numero o escribe  salir:"))
    
    if numero == "salir":
        break
    
    suma = suma + int(numero)
print("la suma total es :",suma)    
