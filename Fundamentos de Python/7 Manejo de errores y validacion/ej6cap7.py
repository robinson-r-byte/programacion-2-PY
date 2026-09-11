#6. Usa un bloque try/except/else/finally para procesar un número ingresado por
#el usuario. El bloque debe: Intentar convertir la entrada a entero.
#Mostrar un mensaje si ocurre un error.Imprimir “Conversión exitosa” en el bloque else.
#Imprimir “Fin del programa” en el bloque finally.

try:
    numero = int(input("Ingrese un nnmero entero: "))
except ValueError:
    
    print("Error: debe ingresar un nnmero entero")
else:
    print("Conversión exitosa")
finally:
    print("Fin del programa")
