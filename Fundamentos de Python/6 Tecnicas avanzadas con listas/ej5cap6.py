#5. Dadas las listas nombres = [’Ana’, ’Luis’, ’Sofía’] y edades = [22, 30, 27],
#usa zip() para imprimir: Ana tiene 22 años, etc.

nombres = ["Ana", "Luis", "Sofía"]
edades = [22, 30, 27]

for nombre, edad in zip(nombres, edades):
    print(nombre, "tiene", edad, "años")