#8. Reescribe el siguiente código dentro de una función 
#llamada mostrar_reporte(nombre,
#edad, ciudad) para que sea reutilizable:
#print ( f " Nombre : ␣{nombre} " )
#print ( f " Edad : ␣{ edad } " )
#print ( f " Ciudad : ␣{ ciudad } " )

def mostrar (nombre,edad,ciudad):
    
    print(f"nombre: {nombre}")
    print ( f" edad : {edad} " )
    print ( f" ciudad : {ciudad}")
    
mostrar("Robinson",23,"Sogamoso")