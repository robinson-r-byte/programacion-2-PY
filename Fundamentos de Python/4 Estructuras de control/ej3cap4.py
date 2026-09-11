#Solicita al usuario dos números y un operador (+, -, *, /). Usa una estructura
#condicional para realizar la operación correspondiente. Si el operador no es válido,
#muestra un mensaje de error.

num1 = float(input("Ingrese el primer numero:"))
num2 = float(input("Ingrese el segundo numero:"))
operador = input("Ingrese el operador")

if operador == "+":
    resultado = num1+num2
    print("El resultado es: ",resultado)
elif operador == "-":
    resultado = num1-num2
    print("El resultado es: ",resultado)
    
elif operador == "*":
    resultado = num1-num2
    print("El resultado es: ",resultado)    
    
elif operador == "/":
    if num2 !=0:
        
        resultado = num1/num2
        print("El resultado es: ",resultado)   
        
    else:
        
        print("Erro no se puede dividir entre cero.")
         
else:
    print("Error OP INVALIDO.") 
            
        
        
     


