#7. Crea una lista con nombres de personas. Usa una comprensión de listas
# para generaruna nueva lista con solo los nombres que tengan más de 4 letras.

nombres = ["Ana","Ricardo", "Luis","Sofia","Juan"]

nombres_largos = [nombre for nombre in nombres if len(nombre) > 4]

print(nombres_largos)