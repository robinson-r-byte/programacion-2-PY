#5. Escribe una función que pida al usuario su edad, la convierta a entero y valide que
#esté en el rango 0–120. Si no es así, muestra un mensaje de advertencia.

def validar_edad():
    edad = int (input("Ingresa la edad"))
    
    if edad >=0 and edad <= 120:
        print("Edad valida")
    else:
        print("Advertencia la edad debe estar en el rango 0-120")    