
def inver():
    palabra = input("\nIngrese una palabra: ").strip().lower()
    if palabra.replace(" ", "").lower().strip().isalpha():
        print(palabra[::-1])
    else:
        print("\ningrese solo letras")
inver()