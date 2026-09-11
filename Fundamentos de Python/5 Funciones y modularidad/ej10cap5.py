#10. Desafío: Crea un pequeño programa modular compuesto por tres funciones:
#-leer_numeros(): pide al usuario ingresar una lista de números separados por
#  comas y los retorna como lista de enteros.
# -calcular_estadisticas(lista): calcula y retorna el mínimo, máximo y promedio.
# -mostrar_resultado(min, max, prom): muestra los resultados al usuario con
#  mensajes claros.
# -Llama las tres funciones en el orden adecuado para que el programa funcione como
#  un todo.

def leer_numeros():
    datos = input("Ingrese numeros separados por comas:")
    lista = [int(numero) for numero in datos.split(",") ]
    return lista

def calcular_estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista)/len(lista)
    
    return minimo, maximo, promedio

def mostrar_resultado(min, max, prom):
    print("minimo",minimo)
    print("Maximo",maximo)
    print("Promedio",promedio)
    
numeros = leer_numeros()

minimo,maximo,promedio =  calcular_estadisticas(numeros)

mostrar_resultado(minimo,maximo,promedio)    
    