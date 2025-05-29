import random
import os
import time
import colorama
from colorama import Fore



def users():
    global usuario1, usuario2, usuario3, contraseña1, contraseña2, contraseña3, Salir, Pasar1, Pasar2, Pasar3, sesion
    usuario1="VACIO" 
    usuario2="VACIO" 
    usuario3="VACIO"
    contraseña1="NONE"
    contraseña2="NONE"
    contraseña3="NONE"
    Salir=True
    Pasar1=False
    Pasar2=False
    Pasar3=False
    sesion="xa"
def ingreso():
    global Pasar1, Pasar2, Pasar3
    if csuser==usuario1 and cspass==contraseña1:
        Pasar1=True
    elif csuser==usuario2 and cspass==contraseña2:
        Pasar2=True
    elif csuser==usuario3 and cspass==contraseña3:
        Pasar3=True
    else:
        print("Ingrese una contraseña y usuario valido")
def u1():
    global usuario1, contraseña1
    if usuario1 !="VACIO":
        print("El usuario esta en uso")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') 

    else:
        usuario1=input("Coloca tu nombre")
        contraseña1=input("Coloca tu contraseña")
        print("Usuario creado")
def u2():
    global usuario2, contraseña2
    if usuario2 !="VACIO":
        print("El usuario esta en uso")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') 
    else:
        usuario2=input("Coloca tu nombre")
        contraseña2=input("Coloca tu contraseña")
        print("Usuario creado")
def u3():
    global usuario3, contraseña3
    if usuario3 !="VACIO":
        print("El usuario esta en uso")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') 

    else:
        usuario3=input("Coloca tu nombre")
        contraseña3=input("Coloca tu contraseña")
        print("Usuario creado")
def borrar():
    os.system('cls' if os.name == 'nt' else 'clear') 
def usuarioo1():
    global kik, llamada, correo
    sesion1=True
    if Pasar1==True:
        while sesion1==True:
            print("Bienvenido,", usuario1)
            kik=int(input("""
                    ---------------------------
                        1.Realizar llamada
                        2.Enviar correo
                        3.Cerrar sesion
                        """))
            borrar()
            match kik:
                case 1:
                    llamada=input("Realiza una llamada aqui")
                    if str(llamada).startswith('9') and len(str(llamada))==9:
                        print(Fore.YELLOW,"Llamando....")
                        time.sleep(1)
                        print(Fore.WHITE, "Llamada exitosa")
                        borrar()
                case 2:
                    correo=input("Envia tu correo")
                    if str(correo).count('@'):
                        print(Fore.YELLOW, "Enviando correo...")
                        time.sleep(1)
                        print(Fore.WHITE, "Correo enviado")
                case 3:
                    print("Cerrando sesion...")
                    time.sleep(1)
                    borrar()
                    sesion1=False
                case _:
                    print()
def usuarioo2():
    global kik, llamada, correo, sesion2
    sesion2=True
    if Pasar2==True:
        while sesion2==True:
            print("Bienvenido,", usuario2)
            kik=int(input("""
                    ---------------------------
                        1.Realizar llamada
                        2.Enviar correo
                        3.Cerrar sesion
                        """))
            borrar()
            match kik:
                case 1:
                    llamada=input("Realiza una llamada aqui")
                    if str(llamada).startswith('9') and len(str(llamada))==9:
                        print(Fore.YELLOW,"Llamando....")
                        time.sleep(1)
                        print(Fore.WHITE, "Llamada exitosa")
                        borrar()
                case 2:
                    correo=input("Envia tu correo")
                    if str(correo).count('@'):
                        print(Fore.YELLOW, "Enviando correo...")
                        time.sleep(1)
                        print(Fore.WHITE, "Correo enviado")
                case 3:
                    print("Cerrando sesion...")
                    time.sleep(1)
                    borrar()
                    sesion2=False
                case _:
                    print()
def usuarioo3():
    global kik, llamada, correo
    sesion3=True
    if Pasar3==True:
        while sesion3==True:
            print("Bienvenido,", usuario3)
            kik=int(input("""
                    ---------------------------
                        1.Realizar llamada
                        2.Enviar correo
                        3.Cerrar sesion
                        """))
            borrar()
            match kik:
                case 1:
                    llamada=input("Realiza una llamada aqui")
                    if str(llamada).startswith('9') and len(str(llamada))==9:
                        print(Fore.YELLOW,"Llamando....")
                        time.sleep(1)
                        print(Fore.WHITE, "Llamada exitosa")
                        borrar()
                case 2:
                    correo=input("Envia tu correo")
                    if str(correo).count('@'):
                        print(Fore.YELLOW, "Enviando correo...")
                        time.sleep(1)
                        print(Fore.WHITE, "Correo enviado")
                case 3:
                    print("Cerrando sesion...")
                    time.sleep(1)
                    borrar()
                    sesion3=False
                case _:
                    print()

users()

while Salir==True:
    try:
        sesion=int(input("""
                        1. Iniciar sesion
                        2. Registrar usuario
                        3. Salir
                        """))
    except Exception:
        print("Solo numeros, no letras")
    match sesion:
        
        case 1:
            borrar()
            csuser=input("Ingrese su usuario ")
            cspass=input("Ingrese su contraseña ")
            ingreso()
            usuarioo1()
            usuarioo2()
            usuarioo3()
        case 2:
            borrar()
            print("""Registrate como usuario
                  1."""    ,usuario1,
                  """2.""" ,usuario2,                  
                  """3.""" ,usuario3,
                  """4. Salir"""
                  """           
                  """)
            try:
                registro=int(input())
                match registro:
                    case 1:
                        u1()
                    case 2:
                        u2()
                    case 3:
                        u3()
            except Exception:
                print("Solo numeros, no letras")
        case 3:
            print("Saliendo....")


        case _:
            print("Ingrese un numero valido")