#2. Dada la lista original = [10, 20, 30], crea:
#Una copia por asignación directa.
#Una copia con .copy().
#Una copia con slicing.
#Modifica un elemento de cada copia y verifica si afecta o no a la lista original.
#Explica el resultado.

original = [10, 20, 30]

copia1 = original
copia2 = original.copy()
copia3 = original[:]

copia1[0] = 100
copia2[1] = 200
copia3[2] = 300

print("Original:", original)
print("Copia 1:", copia1)
print("Copia 2:", copia2)
print("Copia 3:", copia3)