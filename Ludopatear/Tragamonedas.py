import colorama
import random
import os
import time

from colorama import init, Fore, Back, Style
lanzando=8
Creditos=1000
tragamonedas="unboton"
GIG=0
KIK=0
JIK=0
Menu=0
Slot1=0
Slot2=0
Slot3=0
apuesta=100

nombre=(input("Ingresa tu nombre de inversor/a experto"))

while tragamonedas != 4:
    print("Tus creditos:",Fore.YELLOW, Creditos)
    print("Tu apuesta:", Fore.CYAN, apuesta)
    print(Fore.YELLOW, "Si quieres aumentar/bajar la apuesta escribe: 1")
    print("----------------------------------------")
    tragamonedas=(input("Pulsa cualquier boton para tirar..."))

    while tragamonedas=="1":
        print(Fore.YELLOW, "Ajusta tu apuesta")
        print(Fore.YELLOW, "1. 50 Creditos")        
        print(Fore.YELLOW, "2. 100 Creditos")
        print(Fore.YELLOW, "3. 200 Creditos")    
        print(Fore.YELLOW, "4. 500 Creditos")
        print(Fore.YELLOW, "5. 1000 Creditos")        
        print(Fore.YELLOW, "6. 2000 Creditos")    
        print(Fore.YELLOW, "7. 5000 Creditos")  
        print(Fore.YELLOW, "8. Salir")
        Menu=(input())
        if Menu=="1":
            if Creditos>=50:
                print(Fore.CYAN, "Apuesta ajustada a 50 Creditos")
                apuesta=50
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif Creditos<50:
                print(Fore.RED, "No tienes suficientes creditos para realizar esta apuesta")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')                        
        if Menu=="2":
            if Creditos>=100:
                print(Fore.CYAN, "Apuesta ajustada a 100 Creditos")
                apuesta=100
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif Creditos<100:
                print(Fore.RED, "No tienes suficientes creditos para realizar esta apuesta")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
        if Menu=="3":
            if Creditos>=200:
                print(Fore.CYAN, "Apuesta ajustada a 200 Creditos")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                apuesta=200
            elif Creditos<200:
                print(Fore.RED, "No tienes suficientes creditos para realizar esta apuesta")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')                
        if Menu=="4":
            if Creditos>=500:
                print(Fore.CYAN, "Apuesta ajustada a 500 Creditos")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')                
                apuesta=500
            elif Creditos<500:
                print(Fore.RED, "No tienes suficientes creditos para realizar esta apuesta")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
        if Menu=="5":
            if Creditos>=1000:
                print(Fore.CYAN, "Apuesta ajustada a 1000 Creditos")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')                
                apuesta=1000
            elif Creditos<1000:
                print(Fore.RED, "No tienes suficientes creditos para realizar esta apuesta")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
        if Menu=="6":
            if Creditos>=2000:
                print(Fore.CYAN, "Apuesta ajustada a 2000 Creditos")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')                
                apuesta=2000
            elif Creditos<2000:
                print(Fore.RED, "No tienes suficientes creditos para realizar esta apuesta")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
        if Menu=="7":
            if Creditos>=5000:
                print(Fore.CYAN, "Apuesta ajustada a 5000 Creditos")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')                
                apuesta=5000
            elif Creditos<5000:
                print(Fore.RED, "No tienes suficientes creditos para realizar esta apuesta")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
        if Menu=="8":
            print(Fore.YELLOW, "Regresando al menu...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif Menu!="1" or Menu!="2" or Menu!="3" or Menu!="4" or Menu!="5" or Menu!="6" or Menu!="7" or Menu!="8":
            print("Inserte un numero valido")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

    if Creditos>=apuesta and tragamonedas=="":
        
        Creditos=Creditos-apuesta
        for i in range(lanzando):
            Slot1=random.randint(1,10)
            print(Slot1)
            time.sleep(0.003)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        
        for i in range(lanzando):
            Slot2=random.randint(1,10)
            print(Slot1,
                  Slot2)
            time.sleep(0.003)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        for i in range(lanzando):
            Slot3=random.randint(1,10)
            print(Slot1,
                  Slot2,
                  Slot3)
            time.sleep(0.008)
            os.system('cls' if os.name == 'nt' else 'clear')   
        time.sleep(0.05)
        print(Slot1,
              Slot2,
              Slot3
              )
    if Slot1==Slot2==Slot3:
        print(Fore.GREEN, "3 Iguales | GANASTE!")
        print(Fore.YELLOW, "+", apuesta*5, " Creditos")
        Creditos=Creditos+(apuesta*5)
        KIK=KIK+1
    if Slot1==Slot2 or Slot2==Slot3 or Slot1==Slot3:
        print(Fore.GREEN, "2 Iguales | GANASTE!")
        print(Fore.YELLOW, "+", apuesta/2, " Creditos")
        Creditos=Creditos+(apuesta/2)
        GIG=GIG+1
    if Slot1==1 and Slot2==2 and Slot3==3 or Slot1==4 and Slot2==5 and Slot3==6 or Slot1==7 and Slot2==8 and Slot3==9:
        print(Fore.GREEN, "3 en linea | GANASTE!")
        print(Fore.YELLOW, "+", apuesta*10, " Creditos")
        Creditos=Creditos+(apuesta*10)
        JIK=JIK+1
    
    if tragamonedas==4:
        print(Fore.LIGHTYELLOW_EX, "Saliendo del programa...")
    
    elif Creditos<=0:
        print(Fore.RED,"No tienes suficientes creditos...")
    
    if Creditos<=0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN, "FIN DEL JUEGO, TE QUEDASTE SIN CREDITOS")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        break


print(Fore.YELLOW, "Veamos tus puntos...")

if GIG>1:
    print(Fore.YELLOW, "2 Iguales:", GIG)

if KIK>1:
    print(Fore.YELLOW, "3 Iguales:", KIK)

if JIK>1:
    print(Fore.YELLOW, "3 En linea:", JIK)

print(Fore.GREEN, "------------------")
LOP=(GIG * apuesta) + ( JIK * apuesta ) + (KIK*apuesta) 
print(Fore.YELLOW, "Tus puntos:", LOP)

if LOP>10000:
    print(Fore.YELLOW, "Tabla de posiciones")
    print(Fore.CYAN, "1.", nombre, ":",  LOP, "puntos")
    print(Fore.MAGENTA, "2. Mixin : 10000 puntos")

else:
    print(Fore.YELLOW, "Tabla de posiciones")
    print(Fore.MAGENTA, "1. Mixin : 10000 puntos")
    print(Fore.CYAN, "2.", nombre, ":",  LOP, "puntos")   