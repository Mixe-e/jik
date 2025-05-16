# explicacion de match
import colorama

from colorama import Fore
def suma():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    print("El resultado de la suma es", n1+n2)
def resta():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    print("El resultado de la resta es", n1-n2)
def multiplicacion():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    print("El resultado de la multiplicacion es", n1*n2)
def division():
    try:
        n1=int(input("ingrese un numero: "))
        n2=int(input("ingrese un numero: "))
        print("El resultado de la division es", n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        print("Se produjo una excepcion", nombre_de_excepcion)
def calcu():

    while True:
        op=int(input("""Seleccione su opcion
                    1. Suma
                    2. Resta
                    3. Multiplicacion
                    4. Division
                    """))
        match op:
            case 1:
                print(Fore.YELLOW, "Suma")
                suma()
            case 2:
                print(Fore.YELLOW, "Resta")
                resta()
            case 3:
                print(Fore.YELLOW, "Multiplicacion")
                multiplicacion()
            case 4:
                print(Fore.YELLOW, "Division")
                division()
            case 5:
                print(Fore.YELLOW, "Saliendo...")
                break
            case _:
                print(Fore.RED,"Opcion invalida")

calcu()


# finally
# # Codigo a ejecutar siempre



## Menu recursivo, debe tener 3 programas creados anteriormente
## el menu debe llamar a estos programas y ejecutarlos de manera correcta
## debe tener la opcion salir
## y una opcion por defecto






















