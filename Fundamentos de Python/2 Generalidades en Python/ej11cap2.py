# Analice el siguiente código, identifique el error que contiene y proponga una versión
#corregida que permita ejecutar correctamente el programa.
#nombre = input ("¿Cuál es tu nombre ? ")
#edad = input ("¿Cuá ntos años tienes ? ")
#edad_en_10 = edad + 10
#print ( f"{ nombre } , en 10 años tendrás { edad_en_10 } años.")

#le falta el int a la edad     mal  #edad = input ("¿Cuá ntos años tienes ? ")

nombre = input ("¿Cuál es tu nombre ? ")
edad = int(input ("¿Cuá ntos años tienes ? "))  # asi esta bien
edad_en_10 = edad + 10
print ( f"{ nombre } , en 10 años tendrás { edad_en_10 } años.")