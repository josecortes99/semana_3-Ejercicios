
def fun():
    palabra = input("\nIngrese una palabra")
    vocales = "aeiou"
    sem = sum(1 for i in palabra if i in vocales)
    print(sem)
fun()