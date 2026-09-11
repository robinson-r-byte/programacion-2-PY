#3. Escribe una función llamada area_triangulo(base, altura) que calcule y retorne
#el área de un triángulo. Usa la función desde print() para mostrar el resultado al
#usuario.

def area_triangulo(base, altura):
    area = (base * altura) / 2 
    return area

base= float(input("ingrese base:"))
altura= float(input("ingrese altura:"))
   
print("El área del triángulo es:", area_triangulo(base, altura))

