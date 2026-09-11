#4. Escribe una función que reciba dos números y retorne su división. Usa manejo de
#errores para evitar que el programa se detenga si el segundo número es cero. Muestra
#un mensaje apropiado si ocurre división por cero.

def dividir(a,b):
    try:
        resultado = a/b
        return resultado
    
    except ZeroDivisionError:
        print("No se puede dividir en cero")
    
num1=float(input("Ingrese el primer numero:"))    
num2=float(input("Ingrese el segundo numero:"))    

print(dividir(num1,num2))

