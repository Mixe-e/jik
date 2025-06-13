import time
import colorama
from colorama import Fore
import os



#     -5-4-3 -2 -1
# numeros=[7,5,33,24,9]
#      0,1,2,3,4,5


##print(numeros[0])

#for numero in numeros:
#    print("numero ",numero+1)

# print(numeros)

# numeros.append(64)

# print(numeros)

# ##----------------------

# numeros.insert(3,100)

# print(numeros)


##-------------------------------------------


# frutas=["Manzana", "Mango", "Membrillo"]


##------------------------------------------------


# for fruta in frutas:
#     print(fruta)



# nombres=[]
# apellidos=[]
# while True:

#     print("""
#         1. insertar nombre y apellido
#         2. mostrar nombres y apellidos
#         3. Buscar nombre
#         4. Salir
#         """)


#     op=int(input("Seleccione una opcion "))

#     match op:

#         case 1:
#             nom=input("Ingrese un nombre: ")
#             nombres.append(nom)
#             lil=input("Ingrese un apellido: ")
#             apellidos.append(lil)
        
#         case 2:
#             c=0
#             for n in nombres:
#                 print(nombres[c],apellidos[c])
#                 c=c+1
        
#         case 3:            
#             nom=input("Busca el nombre")       
#             if nom in nombres:
#                 print("El nombre,",nom,"Existe")
#             else:
#                 print("El nombre,", nom,"No existe")
        
#         case 4:    
#             break
        
#         case _:
#             print("Opcion invalida")



##-----------------------------------------------

# productos=["Triton", "chocman","pan"]
# precio=[800, 300, 1000]
# while True:

#     lo=int(input("""
#                 1. Ingresar productos
#                 2. Comprar
#                 3. Crear boleta
#                 4. Salir
#                 """))
    
#     match lo:
#         case 1:
#             producto=input("Ingresa un numero producto ")
#             productos.append(producto)
#             precios=input("Ingresa el precio del producto")
#             precio.append(precios)
#         case 2:
#             print("Que vas a comprar?")
#             c=0
#             for prodddddd in productos:
#                 print(productos[c], "$",precio[c])
#                 c=c+1
#         case 3:
#             print("Imprimiendo boleta")

            
#         case 4:
#             break
#         case _:
#             print("Ingrese una opcion valida")


##-------------------------


notas=[7.0,4.6,4.9,7.0,5.6]

op=0
j=5
while True:
    op=int(input("""
        1.- Ingresar notas
        2.- Borrar nota
        3.- Mostrar notas
        4.- Sacar promedio, nota mayor y nota menor
        5.- Limpiar todas las notas
        6.- Salir
        """))
    match op:
        case 1:
            try:
                n=float(input("Ingresa tu nota: "))
                notas.append(n)
                print("Nota ingresada")
                time.sleep(1)
                j=j+1
            except Exception:
                print("Solo numeros, no letras")
        case 2:
            for i, nota in enumerate(notas):
                print(i+1,".-",nota)
            try:
                borrar=int(input("Seleccione la nota a borrar: "))
                notas.pop(borrar-1)
            except Exception:
                print("Solo numeros, no letras")
        case 3:
            print(notas)
        case 4:
            print("Sacando promedio...")
            time.sleep(1)
            promedio=notas/j
            print("Promedio:", promedio)
            time.sleep(1)       
        case 5:
            try:
                decision=int(input("""Esta seguro de querer borrar todas las notas ingresadas?
                    1. Si
                    2. No
                    """))
                if decision==1:
                    notas.clear
                    print("Borrando notas...")
                    time.sleep(2)
                    print("Notas borradas exitosamente")
            except Exception:
                print("Solo numeros, no letras")
            else:
                print("Operacion abortada")
        case 6:
            break
        case _:
            print("ingrese una opcion valida")


















































































































































































