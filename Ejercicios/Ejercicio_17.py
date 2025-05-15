def lanzar_dado_manual():
    entrada = input("Presiona Enter para lanzar el dado")

    total = int(input("Ingrese una longitud: "))
    total += len(entrada)
    
    resultado = (total % 6) + 1
    return resultado


print(lanzar_dado_manual())
