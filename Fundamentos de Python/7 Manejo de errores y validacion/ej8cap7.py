#8. Dado un diccionario con datos de un producto, valida que contenga las claves
#"nombre", "precio" y çantidad". Si falta alguna, muestra un mensaje indicando cuál falta.

producto = {
    "nombre":"laptop",
    "Precio":300000,
    "cantidad":5,    
}

if "nombre" not in producto:
    print("Falta la clave: nombre")

if "precio" not in producto:
    print("Falta la clave: precio")

if "cantidad" not in producto:
    print("Falta la clave: cantidad")