
def fizz():
    num = int(input("\nIngrese un numero: "))
    if num % 3 == 0:
        print("\nFizz")
    elif num % 5 == 0:
        print("\nBuzz")
    else:
        print("\nFizzBuzz")
        
fizz()