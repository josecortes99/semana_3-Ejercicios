import re  

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "La contraseña debe tener al menos 8 caracteres."

    if not re.search("[A-Z]", contraseña):
        return "La contraseña debe contener al menos una letra mayúscula."

    if not re.search("[a-z]", contraseña):
        return "La contraseña debe contener al menos una letra minúscula."

    if not re.search("[0-9]", contraseña):
        return "La contraseña debe contener al menos un número."

    if not re.search("[@#$%^&*]", contraseña):
        return "La contraseña debe contener al menos un símbolo especial (@, #, $, %, etc.)."

    return "La contraseña es segura."

contraseña = input("Ingrese una contraseña: ")
print(validar_contraseña(contraseña))