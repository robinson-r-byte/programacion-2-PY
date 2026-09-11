#5. Declara una variable global llamada contador. 
# Luego, crea una función que la modifique y explique mediante un print()
# si fue necesario usar la palabra clave global.

contador = 0

def comtador ():
    global contador
    
    contador= contador+1
    print("fue necesario usar la palabra clave global.")
    
comtador()
print("Contador:", contador)    

