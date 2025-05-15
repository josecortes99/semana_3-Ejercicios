def palindromo():
    palabra = input("\nIngrese una palabra que se escriba igual al derecho y alrevez:")
    pal = palabra[::-1]
    
    if palabra == pal:
        print("Es un palindromo ")
        print(f"\n{pal}")
    else:
        print("no es palindromo")
    
palindromo()