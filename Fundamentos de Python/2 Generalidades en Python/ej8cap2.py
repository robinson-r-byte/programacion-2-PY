#Una universidad desea saber si un estudiante puede inscribirse a un curso avanzado.
#Para ello, debe cumplir dos condiciones:
#Haber aprobado el curso introductorio.
#Tener un promedio igual o superior a 3.5.
#Escribe un programa que:
#a) Solicite al usuario si aprobó el curso introductorio (sí o no).
#b) Solicite su promedio.
#c) Evalue la condición y muestre directamente True si puede inscribirse o False si no puede.

aprobo = input("aprobo el curso introductorio si o no: ")
promedio = float(input("ingrese el promedio"))

paso = aprobo == "si"  and promedio >= 3.5

print(paso)
