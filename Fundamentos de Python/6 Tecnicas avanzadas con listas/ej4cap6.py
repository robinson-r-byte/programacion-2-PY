#4. Dada la lista colores = [’rojo’, ’verde’, ’azul’], usa enumerate() para imprimir cada
#elemento junto con su índice, en el formato: 0: rojo, 1: verde, etc.

colore = ["rojo","verde","azul"]

for indice, color in enumerate(colore):
    print(indice,":",color)