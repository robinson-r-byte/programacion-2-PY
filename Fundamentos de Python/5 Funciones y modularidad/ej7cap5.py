#Escribe una función llamada imprimir_clave_valor(**kwargs) que reciba 
# cualquier número de argumentos con nombre (clave=valor) e imprima cada 
# clave con su valor en una línea.

def imprimir_clave_valor(**kwargs):
    for clave, valor in kwargs.items():
        print(clave,":",valor)

imprimir_clave_valor(nombre="Robinson", edad=22, carrera="Ingeniería Electrónica")        
        
