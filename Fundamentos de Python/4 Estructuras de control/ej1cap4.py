#Escribe un programa que pida al usuario un número entero y muestre si es positivo,
#negativo o cero usando if, elif y else.

numero = int (input ("Ingrese el numero:"))

if numero > 0:
    print("El numero es positivo")
    
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")        
