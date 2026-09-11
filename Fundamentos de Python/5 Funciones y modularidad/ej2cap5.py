#2. Crea una función llamada es_par(numero) que reciba un número como argumento
#y retorne True si es par o False en caso contrario. Prueba la función con varios
#valores.

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(es_par(3))    
print(es_par(4)) 
print(es_par(5)) 
print(es_par(6)) 
print(es_par(7))
print(es_par(8))  