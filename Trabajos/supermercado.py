total = 0
palta=3000
tomate=2000
naranja=1500
pera=300
Ak47=100000

while True:
    print("1. Palta")
    print("2. Tomate")
    print("3. Naranja")
    print("4. Pera")
    print("5. Ak-47")
    print("6. Salir")
    opcion = int(input("Ingrese una opción (1-5): "))

    if opcion == 1:
        print("Llevaste 1 palta")
        total=total+palta
    elif opcion == 2:
        print("Llevaste 1 tomate")
        total=total+tomate
    elif opcion == 3:
        print("Llevaste 1 naranja")
        total=total+naranja
    elif opcion == 4:
        print("Llevaste 1 pera")
        total=total+pera
    elif opcion == 5:
        print("Llevaste 1 Ak-47")
        total=total+Ak47
    elif opcion == 6:
        break
    else:
        print("Opción no válida")
    opcion = int(input("Ingrese una opción (1-6): "))