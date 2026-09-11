#6. Usa una comprensión de listas para:
#Generar una lista con los cuadrados de los números del 1 al 10.
#Generar una lista con los números pares entre 1 y 20.
#Generar una lista con los primeros diez múltiplos de 3 que sean mayores que 10.

cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)

pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)
 
multiplos = [x for x in range(12, 42, 3)][:10]
print(multiplos)