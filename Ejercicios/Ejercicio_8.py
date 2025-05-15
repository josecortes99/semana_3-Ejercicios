def contar():
    palabra = input("\nIngrese una palbra: ")
    letra =  input("\nCual letra quiere buscar para ver cuantas veces esta?: ")
    pa = palabra.count(letra)
    print(f"\nVeces respetida: {pa}")
contar()