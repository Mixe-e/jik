import time
import colorama
from colorama import Fore
import os
import random


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

## notas

# notas=[7.0,4.6,4.9,7.0,5.6]

# op=0
# j=5
# while True:
#     op=int(input("""
#         1.- Ingresar notas
#         2.- Borrar nota
#         3.- Mostrar notas
#         4.- Sacar promedio, nota mayor y nota menor
#         5.- Limpiar todas las notas
#         6.- Salir
#         """))
#     match op:
#         case 1:
#             try:
#                 n=float(input("Ingresa tu nota: "))
#                 notas.append(n)
#                 print("Nota ingresada")
#                 time.sleep(1)
#                 j=j+1
#             except Exception:
#                 print("Solo numeros, no letras")
#         case 2:
#             for i, nota in enumerate(notas):
#                 print(i+1,".-",nota)
#             try:
#                 borrar=int(input("Seleccione la nota a borrar: "))
#                 notas.pop(borrar-1)
#             except Exception:
#                 print("Solo numeros, no letras")
#         case 3:
#             print(notas)
#         case 4:
#             print("Sacando promedio...")
#             time.sleep(1)
#             suma= sum(notas)
#             totalnotas = len(notas)
#             promedio= suma /totalnotas
#             print("Promedio:", promedio)
#             time.sleep(1)
#             print("La nota mayor es:", notas[-1])
#             print("La nota menor es:", notas[0])
#         case 5:
#             try:
#                 decision=int(input("""Esta seguro de querer borrar todas las notas ingresadas?
#                     1. Si
#                     2. No
#                     """))
#                 if decision==1:
#                     notas.clear()
#                     print("Borrando notas...")
#                     time.sleep(2)
#                     print("Notas borradas exitosamente")
#             except Exception:
#                 print("Solo numeros, no letras")
#             else:
#                 print("Operacion abortada")
#         case 6:
#             break
#         case _:
#             print("ingrese una opcion valida")



##---------------------------------------------------



# vero=[
#                 [3,4]
#                 [8,9,64,8]
#                     ]

# print(vero [1][2])

####----------------------------------------------- 


# def ruleta():
#     barril=random.randint(1,6)
#     rul=int(input("Dispara"))

#     while rul!=barril:
#         rul=int(input("Dispara"))
#     print("BANG!!")

# def suma_ret():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(n1+n2)




# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     return n1+n2


# def suma_arg(n1,n2):
#     print(n1+n2)



# suma()
# num=suma_ret()
# print(num*5)

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese otro numero: "))
# suma_arg(num1, num2)
# print("El numero es,", suma_arg , (num1,num2)*2)




# def numero():
#     n=int(input("Ingrese un numero"))
#     return n*0.19

# def desc(precio, porc):
#     return precio*(porc/100)


##------------------------------------------


# productos=[

#     {"nombre":"lapiz", "precio": 400},
#     {"nombre":"goma", "precio": 300},
#     {"nombre":"estuche", "precio": 1600}
# ]


# print(productos[2]["nombre"])


# for item in productos:
#     print(f"El articulo, " {item["nombre"]} "tiene un precio de" {item} "p")



##-----------------------
precio=[]
productos=[]


while True:
    decision=int(input("""
                    1. Agregar articulo
                    2. Borrar articulo
                    3. Actualizar articulo
                    4. Mostrar listado de articulos
                    5. Salir
            """))





    match decision:
        case 1:
            articulo=input("Agrega un articulo")
            productos.append(articulo)
            precios=int(input("Agregale un precio"))
            precio.append(precios)
        case 2:
            c=0
            for i,prodc in enumerate(productos):
                print(i,".-", productos[c], precio[c])
                c=c+1
            borrar=int(input("Seleccione producto a borrar"))
            productos.pop(borrar)
            precio.pop(borrar)
        case 3:
            c=0
            for i in productos:
                c=c+1
                print(productos[c], precio[c])
            articulo=input("Agrega un articulo")
            precios=int(input("Agregale un precio"))
        case 4:
            c=0
            for i, prod in enumerate(productos):
                print(productos[c], precio[c])
                c=c+1
        case 5:
            break
        case _:
            print("Opcion invalida")










