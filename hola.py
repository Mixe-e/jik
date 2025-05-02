

# # Ingreso de variables

# print("ingrese su nombre")
# nombre=input()
# print("ingrese su edad")
# edad=input()

# print("holaaaa ,",nombre, "y su edad es", edad)

# # Suma

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# print(n1+n2)

# # Multiplicacion

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# print("La multiplacion de estos numeros da", n1*n2)


# # Promedio de 3 numeros

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# n3=int(input("ingrese un numero "))
# n4=n1+n2+n3

# if n4>=40:
    # print("el alumno aprobo")
# else:
    # print("el alumno reprobo")

# print("El promedio es", n4/3)

## Edad ingresar 

# edad=int(input("ingrese su edad"))
# if edad>=18:
    # print("usted es mayor de edad")

# elif edad>=12 and edad=<18:
    # print("Usted es adolescente")
# elif edad>=18 and edad=<65:
    # print("Usted es un adulto")
# else edad>65
    # print("Usted es un viejo")





# # Inicio de tabla de multiplicar

# cant=int(input("ingrese la cantidad de repeticiones "))
# for i in range(cant):
    # print("Esta es la table del ", i)
    # for j in range(1,10):
        # print(i, "*", j, "=", i*j)


# # Fin Para

# nombre=input("ingrese su nombre")
# edad=input("ingrese su edad")
# print("hola", nombre, "su edad es", edad)


# num=int(input("ingrese un numero"))

##--------------------------------------------------------------------
# # Sacar promedio definido por el usuario

# cant=int(input("ingrese la cantidad de notas"))
# total=0
# notasazules=0
# for i in range(cant):
#    print("ingrese la nota", i+1)
#    nota=float(input(""))
#    total=total+nota
#    if nota>=4:
#        notasazules=notasazules+1
# promedio=total/cant
# print("el promedio es", promedio)
# print("la cantidad de notas azules son:", notasazules)
# if promedio>=4:
#    print("el alumno aprobo")
# else:
#    print("el alumno reprobo")

##--------------------------------------------------------------------
## Clave1234

# clave=1234
# y=3
# for i in range(3):
#     pas=int(input("ingrese la clave"))
    
#     if clave==pas:
#             print("blenvenido al sistema")
#             break
#     else:
#         y=y-1
#         print("clave incorrecta, quedan", y , "intentos")


##--------------------------------------------------------------------

# total = 0
# palta=3000
# tomate=2000
# naranja=1500
# pera=300
# Ak47=100000

# while True:
#     print("1. Palta")
#     print("2. Tomate")
#     print("3. Naranja")
#     print("4. Pera")
#     print("5. Ak-47")
#     print("6. Salir")
#     opcion = int(input("Ingrese una opción (1-5): "))

#     if opcion == 1:
#         print("Llevaste 1 palta")
#         total=total+palta
#     elif opcion == 2:
#         print("Llevaste 1 tomate")
#         total=total+tomate
#     elif opcion == 3:
#         print("Llevaste 1 naranja")
#         total=total+naranja
#     elif opcion == 4:
#         print("Llevaste 1 pera")
#         total=total+pera
#     elif opcion == 5:
#         print("Llevaste 1 Ak-47")
#         total=total+Ak47
#     elif opcion == 6:
#         break
#     else:
#         print("Opción no válida")
#     opcion = int(input("Ingrese una opción (1-6): "))


# print("total de palta:", palta)
# print("total de tomate:", tomate)
# print("total de naranja:", naranja)
# print("total de pera:", pera)
# print("total de Ak-47:", Ak47)
# print("El total es:", total)
# print("Gracias por su compra")


##---------------------------------------------------------

import random

# numAzar=random.randint(1,50)
# adivinar=int(input("Adivina el numero"))

# while adivinar!=numAzar:

#     if adivinar>numAzar:
#         print("El numero es menor")
#         print(numAzar)
#         adivinar=int(input("Adivina el numero"))

#     if adivinar<numAzar:
#         print("El numero es mayor")
#         print(numAzar)
#         adivinar=int(input("Adivina el numero"))

#     if adivinar==numAzar:
#         print("Adivinaste yippie")
#         break


##-----------------------------------------------------------
## arreglar codigo -
# import random
# import time


# barril=random.randint(1,6)
# rul=int(input("Dispara"))

# while barril!=rul:

# print("Salvada")
# rul=int(input("Dispara"))

#     if barril==rul:
#         print("Moriste")
#         break

##------------------------------------------------------------
# import random
# import time

# j1=0
# j2=0
# meta=30
# kik=0

# Jugador1=(input("Ingresa nombre del jugador 1"))
# time.sleep(1)
# Jugador2=(input("Ingresa nombre del jugador 2"))

# while meta!=6999:
#     kik=kik+1

#     if kik % 2 == 0:
#         print("turno de:", Jugador1)
#         time.sleep(1)
#         numazar=random.randint(1,7)
#         j1=j1+numazar
#         print(Jugador1, " tiro el dado y salio:", numazar)
#         print(Jugador1, j1)
#         time.sleep(1)
#         if j1>=30:
#             print(Jugador1, " gano")
#             break
      
#     else:
#         print("turno de:", Jugador2)
#         time.sleep(1)
#         numazar=random.randint(1,7)
#         j2=j2+numazar
#         print(Jugador2, "tiro el dado y salio:", numazar)
#         print(Jugador2, j2)
#         time.sleep(1)
#         if j2>=30:
#             print(Jugador2, " gano")
#             break

##--------------------------------------------------------

##arancel

# arancel=200000
# descuento=0

# print("""
#     1. Puente alto
#     2. La florida
#     3. La pintana
#     4. San joaquin
#       """)
# comuna=int(input("Ingrese su comuna"))


# while comuna!=7:

#     if comuna==1:
#         print("descuento aplicado 25%")
#         descuento=descuento+25
#         break
#     if comuna==2:
#         print("descuento aplicado 20%")
#         descuento=descuento+20
#         break
#     if comuna==3:
#         print("descuento aplicado 30%")
#         descuento=descuento+30
#         break
#     if comuna==4:
#         print("descuento aplicado 15%")
#         descuento=descuento+15
#         break
#     else:
#         print("ingrese un numero valido")
#         comuna=int(input("Ingrese su comuna"))


# print("con cuantas personas vive?")
# print("""
#     1. 1 persona
#     2. De 2 a 4 personas
#     3. 5 personas o más
#       """)
# personas=int(input("ingrese cantidad de personas"))

# while personas!=7:

#     if personas==1:
#         print("descuento aplicado 2%")
#         descuento=descuento+2
#         break
#     if personas==2:
#         print("descuento aplicado 3%")
#         descuento=descuento+3
#         break
#     if personas==3:
#         print("descuento aplicado 4%")
#         descuento=descuento+4
#         break
#     else:
#         print("ingrese un numero valido")
#         personas=int(input("Ingrese cantidad de personas"))



# print("Su comuna", comuna)
# print("Cantidad de personas", personas)
# print("Descuento aplicado para su arancel%", descuento)
# print("Arancel:", arancel)
# descuentoinicial=arancel*descuento/100
# Darancel=arancel-descuentoinicial
# print("Descuento aplicado al arancel%", descuentoinicial)
# arancel=arancel-Darancel
# print("El total a pagar es:", Darancel)

##-----------------------------------------------------------

# import time


# contraseña="eroigjerojersohierjhoieruoeugjerorgjrogpeiohbboisebeobe"

# print("Bienvenido al cajero")
# print("""
#     Este cajero solo puede dar billetes en multiplos de 5000, desea continuar?
#       """)


# decision=int(input("1. Si | 2. No"))


# while decision!=contraseña:
    
#     if decision==1:
#         monto=int(input("Inserte el monto"))

#     if decision==2:
#         print("Saliendo del sistema...")
#         break
    
#     else:
#         print("Ingrese un numero valido")
#         decision=int(input("1. Si | 2. No"))

##-----------------------------------------------------------

print("Bienvenido al supermercado")
kik="tilinsin"
categorias=(int(input("Seleccione categoria")))

while categorias!=kik:
    print("""
        1. Energeticas  
        2. Gatitos 
        3. Galletas          
          """)

    if categorias==1:
    
        print("Seleccione producto")
        print("""     
            1. Energetica morada
            2. Energetica azul   
            """)
        energetica=(int(input))
        if energetica==1:
            energeticamorada=energeticamorada+1
        if energetica==2:
            energeticaazul=energeticaazul+1

    if categorias==2:
        print("Seleccione producto")
        print("""     
            1. Gatito azul
            2. Gatito naranja   
            """)
        gatito=(int(input))
        if gatito==1:
            gatitoazul=gatitoazul+1
        if gatito==2:
            gatitonaranja=gatitonaranja+1

    if categorias==3:
        print("Seleccione producto")
        print("""     
            1. Serranita
            2. carioca   
            """)
        galleta=(int(input))
        if galleta==1:
            serranita=serranita+1
        if galleta==2:
            carioca=carioca+1

       


