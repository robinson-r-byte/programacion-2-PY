#8. Desafío: Dadas dos listas:
#productos = [ "Pan " , " Leche " , " Huevos " ]
#precios = [ 1 5 0 0 , 3200 , 5200]
#Usa zip() para generar una lista de cadenas en el formato "Pan: $1500", y luego
#una comprensión de listas para filtrar solo los productos cuyo precio sea mayor a
#$3000.

productos = ["Pan","Leche ", "Huevos"]
precios = [1500,3200,5200]

lista = [f"{producto}:{precios}" for producto,precio in zip(productos,precios)]

print(lista)

mayores = [producto for producto,precio in zip(productos,precios)if  precio > 3000]

print(mayores)