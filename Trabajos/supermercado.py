total = 0
palta=3000
tomate=2000
naranja=1500
pera=300
Ak47=100000
op=0
name="sinnombre"
nombresaso=False

import os


def supermercado():
    global total, pa, to, na, pe, ak, name
    while True:
            try:
                print("""
                      1. Palta
                      2. Tomate
                      3. Naranja
                      4. Pera
                      5. AK47
                      6. Salir
                      7. Escribe nombre      
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
                        to=to+1
                    case 3:
                        print("Llevaste 1 naranja")
                        total=total+naranja
                        na=na+1
                    case 4:
                        print("Llevaste 1 pera")
                        total=total+pera
                        pe=pe+1
                    case 5:
                        print("Llevaste 1 Ak-47")
                        total=total+Ak47
                        ak=ak+1
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

print("Paltas:", pa)
print("Tomate:", to)
print("Naranja:", na)
print("Pera", pe)
print("Ak-47", ak)
if nombresaso==True:
    print("Gracias por su compra", name)


