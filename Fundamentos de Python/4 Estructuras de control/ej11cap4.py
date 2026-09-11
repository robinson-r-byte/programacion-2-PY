#11. Usa un ciclo for y la sentencia break para recorrer una lista de números. 
# El ciclo debe detenerse al encontrar un número negativo, e imprimir un mensaje indicando
#que se encontró

numeros = [2,4,34,2,3,45,-5,24,13]

for num in numeros:
    if num < 0:
        print("Se encontro un numero negativo.")
        break
    
    print(num)