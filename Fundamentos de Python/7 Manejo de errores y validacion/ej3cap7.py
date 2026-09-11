#3. Modifica el ejercicio anterior para que capture múltiples excepciones: una por ValueError
#y otra por cualquier otro tipo de error inesperado. Usa un mensaje distinto para
#cada caso.
try:
    numero = int(input("Ingrese numero entero:"))
    print("Numero ingresado:",numero)
    
    
except ValueError:
    print("la entrada debe ser un numero")

except Exception:
    print("Ocurrió un error inesperado")    