def generar_contraseña(longitud):
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*"
    contraseña = ""

    for i in range(longitud):
        contraseña += caracteres[i % len(caracteres)]  

    return contraseña

longitud = int(input("Ingrese la longitud de la contraseña: "))
print("🔐 Contraseña generada:", generar_contraseña(longitud))