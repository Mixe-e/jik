def opciones():
    global op, Total, Salmon, Palta, Kanikama, Hand, kik, kij, productos, sal, han, pal, kal, Totald
    op=0
    Total=0
    Totald=0
    Salmon=8000
    Palta=5000
    Kanikama=3000
    Hand=2500
    kik= False
    kij=False
    productos=0
    sal=0
    han=0
    pal=0
    kal=0
def importar():
    global colorama, time, os, Fore
    
    import colorama
    import time
    import os
    from colorama import Fore
def boleta():
    global productos, sal, pal, kal, han, Total, kij, Total, Totald
    
    print("Total de productos:", productos)
    print("-------------------------------")
    print("Sushi Salmon:", sal)
    print("Sushi Palta:", pal)
    print("Sushi Kanikama:", kal)
    print("Handroll:", han)
    print("-------------------------------")
    print("Total a pagar: ", Total)
   
    if kij==True:
        Totald=Total*10/100
        print("Descuento aplicado %10:", Totald)
        Total=Total-Totald
        print("-------------------------------")
        print("Total a pagar:", Total)


importar()
opciones()






while kik == False:
    print(Fore.YELLOW, "Bienvenido a la tilin tienda sushi")
    print(Fore.WHITE, """
        1. Sushi salmon $8000
        2. Sushi Palta $5000
        3. Sushi kanikama $3000
        4. Handroll $2500
        5. Terminar pedido
        """)
    op=int(input(""))
    match op:
            case 1:
                print("Seleccione cuantos Sushi salmon desea llevar")
                multiplicador=int(input(""))
                Total=Total+Salmon*multiplicador
                productos=productos+multiplicador
                sal=sal+multiplicador
            case 2:
                print("Seleccione cuantos Sushi palta desea llevar")
                multiplicador=int(input(""))
                Total=Total+Palta*multiplicador
                productos=productos+multiplicador
                pal=pal+multiplicador
            case 3:
                print("Seleccione cuantos Sushi kanikama desea llevar")
                multiplicador=int(input(""))
                Total=Total+Kanikama*multiplicador
                productos=productos+multiplicador
                kal=kal+multiplicador
            case 4:
                print("Seleccione cuantos Handroll desea llevar")
                multiplicador=int(input(""))
                Total=Total+Hand*multiplicador
                productos=productos+multiplicador
                han=han+multiplicador
            case 5:
                break
            case _:
                print("Por favor seleccione un numero valido")



Desc=int(input("""Posee un codigo de descuento?
               1. Si
               2. No
               """))
if Desc == 1:
    while True:
        Aplicardesc=(input("Escriba su descuento, para salir escriba el X: "))
        
        if Aplicardesc=="soyotaku":
            print("Codigo de descuento aplicado: 10%")
            kij=True
        elif Aplicardesc=="X" or Aplicardesc=="x":
            break
        else:
            print("Ingrese un codigo valido")


boleta()
