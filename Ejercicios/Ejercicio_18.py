def suma_elementos_unicos(lista):
    unicos = list(set(lista))  
    return sum(unicos)  

lista = [10, 20, 20, 30, 40, 40, 50]
resultado = suma_elementos_unicos(lista)
print("Suma :", resultado)