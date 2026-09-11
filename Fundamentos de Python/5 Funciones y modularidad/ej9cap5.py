#9. Define una función llamada es_primo(n) que retorne True si el número es primo,
#y False si no lo es. Usa la función dentro de un ciclo for para imprimir todos los
#números primos entre 1 y 50.


def primo(n):
    if n < 2:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True

for numero in range (1,51):
    if primo(numero):
        print(numero)

    