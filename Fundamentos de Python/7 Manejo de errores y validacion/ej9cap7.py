def ingresar_nota():
    nota = int(input("ingrese una nota:"))

    if 0.0 <= nota <= 5.0:
        return nota
    else:
        print("La nota debe estar entre 0.0 y 5.0")


nota = ingresar_nota()
print("Nota ingresada:", nota)