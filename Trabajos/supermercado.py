total = 0
palta=3000
tomate=2000
naranja=1500
pera=300
Ak47=100000
op=0
name="sinnombre"
nombresaso=False
def supermercado():
    
        while True:
            try:
                print("""
                      1. Palta
                      2. Tomate
                      3. Naranja
                      4. Pera
                      5. AK47
                      6. Salir      
                      """)
                op = int(input("Ingrese una opción (1-5): "))

                match op:
                    
                    case 1:    
                        print("Llevaste 1 palta")
                        total=total+palta
                        pa=pa+1
                    case 2:
                        print("Llevaste 1 tomate")
                        total=total+tomate
                    case 3:
                        print("Llevaste 1 naranja")
                        total=total+naranja
                    case 4:
                        print("Llevaste 1 pera")
                        total=total+pera
                    case 5:
                        print("Llevaste 1 Ak-47")
                        total=total+Ak47
                    case 6:
                        break
                    case 7:
                        name=input("Escriba su nombre")
                        nombresaso=True
                    case _:
                        print("Opción no válida")
            except Exception:
                print("Solo numeros no texto")


supermercado()


def salida():
    print("Total:", total)


if nombresaso==True:
    print("Gracias por su compra", name)


salida()