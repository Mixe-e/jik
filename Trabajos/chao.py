import colorama
from colorama import Fore
import random
import time
import os

# kanye=0
# trump=0
# while True:
#     voto = input("Escribe 'k' para Kanye o 't' para Trump (o 'q' para salir): ")
#     if voto == 'k':
#         kanye += 1
#         print("Has votado por Kanye.")
#     elif voto == 't':
#         trump += 1
#         print("Has votado por Trump.")
#     elif voto == 'q':
#         break
#     else:
#         print("Opción no válida. Intenta de nuevo.")
# print("Resultados de la votación:")
# print("Kanye:", kanye)
# print("Trump:", trump)
# print("Gracias por participar en la votación.")
# if kanye > trump:
#     print("Kanye ha ganado la votación.")
# elif trump > kanye:
#     print("Trump ha ganado la votación.")

##----------------------------------------------------------------------------------------------

# botella=600
# sed=True


# while botella>=0 and sed:
#     Beber=input(Fore.YELLOW, "Tomar agua")
#     print(Fore.CYAN, "GLU GLU")
#     botella-= random.randint(20,60)
#     print("Queda,",botella, Fore. CYAN, "ml")
#     resp=input(Fore.YELLOW, "Aun tiene sed?")
#     if resp=="no":
#         sed=False
#     time.sleep(1)


##--------------------------------------------------------------------------------------

# cocholate=1

# if cocholate>=1:

#     print(Fore.YELLOW, "Si hay chocolate")
#     cocholate=cocholate-1
# else:
#     print(Fore.CYAN, "Se acabo, ese era el ultimo...")

##-------------------------------------------------------------------------

# print(Fore.WHITE, "Salio gta seis? 1.Si | 0.No")
# gta6=(int(input("")))
# if gta6==1:
#     print(Fore.YELLOW, "GTA 6 HA SALIDO")
# elif gta6==0:
#     print(Fore.RED, "Nos vemos hasta 2026 pelotudo")
# else:
#     print("Insertar numero valido")
#     gta6=(int(input("")))

##---------------------------------------------------


# Credito=0
# Educacion=0

# print("""
#     Ingrese su cantidad de ingresos
#     -------------------------
#     1. Entre 500000 y 1000000
#     2. Entre 1000000 y 1500000
#     3. Mas de 1000000
#     """)
# Ingresos=(int(input("")))


# if Ingresos==1:
#     Credito=Credito+300000

# elif Ingresos==2:
#     Credito=Credito+650000

# elif Ingresos==3:
#     Credito=Credito+1000000

# elif Ingresos>=4:
#     print("Ingrese un numero valido")
#     Ingresos=(int(input("")))


# print("""
#     Ingrese su nivel educacional
#     -------------------------
#     1.Basica
#     2.Media  
#     3.Superior
#     """)
# Educacion=(int(input("")))
    
# if Educacion==1:
#     Credito=Credito*1
    
# elif Educacion==2:
#     Credito=Credito*1.3

# elif Educacion==3:
#     Credito=Credito*1.5

# elif Educacion>=4:
#     print("Insertar numero valido")
#     Educacion=(int(input(Fore.YELLOW,"")))



# print("""
#     Ingrese su nacionalidad
#     -------------------------
#     1.Chileno/a
#     2.Extranjero/a 
#     """)
# Nacionalidad=(int(input("")))

# if Nacionalidad==1:
#     Credito=Credito+300000
    



# print("SU CREDITO FINAL ES DE.....")
# time.sleep(2)

# if Credito>300000:
#     print(Fore.YELLOW, Credito, "Credito")

# else:
#     print(Fore.RED, Credito, "Credito")

##------------------------------------------------------


# digito1=(int(input("Digito 1: Escriba un numero")))

# digito2=(int(input("Digito 2: Escriba un numero")))

# while digito2<digito1:
#     print(Fore.RED, "El ultimo digito es menor al 1, porfavor insertar un numero mayor al digito 1")
#     print(Fore.CYAN, "-------------------------------------------------------")
#     digito2=(int(input(Fore.CYAN, "Digito 2: Escriba un nuevo digito")))

# digito3=random.randint(digito1,digito2)

# for i in range(digito3):
#     print(Fore.YELLOW, "▄")


# print(Fore.CYAN, "-------------------------------------------------------")
# print(Fore.CYAN, "Se imprimio el ▄", digito3, "veces")

##---------------------------------------

# def valores():
#     global conejos, per, pero
#     conejos=2
#     per=0
#     pero=0
# valores()

# while True:
#     try:
#         perros=int(input("Cuantos perros de caza son? "))
#         print("Cuota minima de conejos:", conejos)
#         for i in range(perros):
#             i=i+1
#             print("Perro:", i)
#             cuota=random.randint(0,6)
#             time.sleep(1)
#             if cuota>conejos:
#                 print("El perro", i ,"Cumplio la cuota: ", cuota)
#                 per=per+1
#             else:
#                 print("El perro", i ,"se quedo sin filete por no cumplir la cuota: ", cuota)
#                 pero=pero+1
#         print("------------------------------------")
#         print("Resumen...")
#         time.sleep(1)
#         print(Fore.YELLOW, "Perros que cumplieron la cuota: ", per)
#         print(Fore.CYAN, "Perros que no cumplieron la cuota: ", pero)
#     except Exception:
#         print("Solo numeros enteros")


##------------------------------------------------
def valores():
    global autos, op, oplavado, standard, full,basico, fullp, basicop, standardp
    fullp=0
    basico=0
    full=0
    op=0
    oplavado=0
    autos=0
    standard=0
    basicop=0
    standardp=0
valores()
def fulll():
    global full, fullp, autos
    full=full+1
    fullp=fullp+15000
    autos=autos+1
def standardd():
    global standard, standardp, autos
    standard=standard+1
    standardp=standardp+10000
    autos=autos+1
def basicoo():
    global basico, basicop, autos
    basico=basico+1
    basicop=basicop+7000
    autos=autos+1
def finalizacion():
    global autos, full, standard, basico, fullp, standardp, basicop
    print("Autos que ingresaron:", autos)
    print("-----------------------------")
    print("Autos que usaron el lavado full: ",full)
    print("Autos que usaron el lavado Standard: ",standard)
    print("Autos que usaron el lavado Básico: ",basico)
    print("--------------------------------")
    print("Full $", fullp)
    print("Standard $", standardp)
    print("Básico $", basicop)
    print("Total $", fullp+standardp+basicop)
    print("----------------------")
    if fullp>standardp and fullp>basicop:
        print("El monto mas alto fue", fullp, "del servicio full")
    elif standardp>fullp and standardp>basicop:   
        print("El monto mas alto fue", standardp, "del servicio standard")
    elif basicop>fullp and basicop>standardp:
        print("El monto mas alto fue", basicop, "del servicio básico")
            
while True:
    print("""Lavado de autos
          -----------------------
          1. Pago del lavado
          2. Ver ventas diarias
          3. Salir
          """)
    op=int(input())
    match op:
        case 1:
            print("""Elija su nivel de lavado
                  1. Full | $15.000
                  2. Standard | $10.000
                  3. Básico | $7.000
                  4. Salir
                  """)
            oplavado=int(input())
            match oplavado:
                case 1:
                    print("Lavado a full, espere un momento...")
                    time.sleep(3)
                    fulll()
                case 2:
                    print("Lavado Standard, espere un momento...")
                    time.sleep(3)
                    standardd()
                case 3:
                    print("Lavado Básico, espere un momento...")
                    time.sleep(3)
                    basicoo()
                case 4:
                    print("Saliendo....")
                    time.sleep(1)
                case _:
                    print("Seleccione un numero valido")
        case 2:
            finalizacion()
        case 3:
            print("Saliendo del sistema...")
            time.sleep(1)
            break
                
        case _:
            print("Seleccione un numero valido")








