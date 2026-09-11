#Dado un texto, cuenta cuántas veces aparece la letra “a” (minúscula) 
#usando unciclo for

texto= input("Escribe la letra texto:")

contador = 0

for letra in texto:
    if letra == "a":
        contador += 1

print(f"La letra a aparece {contador} veces")        
