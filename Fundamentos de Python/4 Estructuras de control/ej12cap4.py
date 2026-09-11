#12. Desafío: Escribe un programa que simule un cajero automático. El usuario inicia con
#    $500. En cada iteración puede retirar un monto ingresado por teclado. 
#    El ciclo termina si el usuario escribe 0 o si el saldo es insuficiente. Muestra 
#    el saldo actualizadodespués de cada retiro y un mensaje final al terminar


saldo = 500

while saldo > 0:
    retiro = int(input("Ingrese el monto para retirar(0 para salir):"))
    
    if retiro == 0:
        break
    if retiro > saldo:
        print("monto insuficiente")
        break
    
    saldo = saldo - retiro
    
    print("saldo actual ",saldo)

print("saldo final",saldo)    
    
    