#2. Escribe un programa que intente convertir una cadena ingresada por el usuario a
#entero. Si ocurre un error, muestra el mensaje: .
#Entrada inválida: debe ser un número entero".

try:
    numero = int(input("Ingrese numero entero:"))
    print("Numero ingresado:",numero)
    
    
except ValueError:
    print("la entrada debe ser un numero")
