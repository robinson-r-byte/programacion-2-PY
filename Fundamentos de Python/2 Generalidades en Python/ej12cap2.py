# Analice el siguiente código, identifique el error que contiene y proponga una versión
# corregida. El programa busca determinar si al usuario le alcanza el dinero para
# comprar un teléfono que cuesta 1’199.999,99.
# 1 dinero_usuario = input ("¿De cuánto dinero dispones ? ")
# 2 precio = 1199999.99
# 3 print ( dinero_usuario > precio )

#esta mal por q faltaba escribir float ya q es precios para q este bien

dinero_usuario = float(input ("¿De cuánto dinero dispones ? "))   
precio = 1199999.99
print ( dinero_usuario > precio )


