#7. Dado el diccionario notas = {’Ana’: 4.5, "Luis": 3.7, "Pedro": 4.2},
#escribe un programa que imprima todos los nombres y notas en el formato: Luis tiene
#una nota de 3.7.

notas = {
    "Ana": 4.5,
    "Luis": 3.7,
    "Pedro": 4.2       
}

for nombre, nota in notas.items():
    print(nombre,"tiene una nota de",nota)