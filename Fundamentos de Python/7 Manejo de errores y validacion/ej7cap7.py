#7. Escribe un programa que use assert para verificar que una lista no esté vacía antes
#de calcular su promedio. Si la lista está vacía, debe mostrar el mensaje: "La lista
#no puede estar vacía".

numeros = [1,2,3,4,5]

try:
    assert len(numeros) > 0
    promedio = sum(numeros) / len(numeros)
    print("El promedio es:", promedio)

except AssertionError:
    print("la lista no puede estar vacia")    