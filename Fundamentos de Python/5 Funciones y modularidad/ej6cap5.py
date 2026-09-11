def sumar (*args):
    suma = 0
    
    for numero in args:
        suma += numero
        
    return suma

print(sumar(1,2,3))    
print(sumar(1,2,3,4,5))    
print(sumar(1,2,3,4,5,6,7))    
