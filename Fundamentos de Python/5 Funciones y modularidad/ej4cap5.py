#Escribe una función saludo_personalizado(nombre, mensaje) que imprima un
#saludo con nombre y un mensaje opcional. Si no se proporciona mensaje, debe usar
#“¡Que tengas un buen día!” por defecto. Prueba la función con y sin el segundo
#argumento.

def saludo_personalizado(nombre, mensaje="¡Que tengas un buen día!"):
    print(f"hola{nombre},{mensaje} como estas")

saludo_personalizado("Robinson", "Espero que estés muy bien.")    
saludo_personalizado("Robinson")