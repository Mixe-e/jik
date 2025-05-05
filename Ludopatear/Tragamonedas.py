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


nombre=(input("Ingresa tu nombre de inversor/a experto"))

while tragamonedas != 4:
    print("Tus creditos:",Fore.YELLOW, Creditos)
    print("----------------------------------------")
    tragamonedas=(input("Pulsa cualquier boton para tirar..."))
    if Creditos>=100:  
        
        Creditos=Creditos-100
        for i in range(lanzando):
            Slot1=random.randint(1,10)
            print(Slot1)
            time.sleep(0.010)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        
        for i in range(lanzando):
            Slot2=random.randint(1,10)
            print(Slot1)
            print(Slot2)
            time.sleep(0.010)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        for i in range(lanzando):
            Slot3=random.randint(1,10)
            print(Slot1)
            print(Slot2)
            print(Slot3)
            time.sleep(0.018)
            os.system('cls' if os.name == 'nt' else 'clear')   
        time.sleep(0.05)
        print(Slot1)
        print(Slot2)
        print(Slot3)
    if Slot1==Slot2==Slot3:
        print(Fore.GREEN, "3 Iguales | GANASTE!")
        print(Fore.YELLOW, "+1000 Creditos")
        Creditos=Creditos+1000
        KIK=KIK+1
    if Slot1==Slot2 or Slot2==Slot3 or Slot1==Slot3:
        print(Fore.GREEN, "2 Iguales | GANASTE!")
        print(Fore.YELLOW, "+50 Creditos")
        Creditos=Creditos+50
        GIG=GIG+1
    if Slot1==1 and Slot2==2 and Slot3==3 or Slot1==4 and Slot2==5 and Slot3==6 or Slot1==7 and Slot2==8 and Slot3==9:
        print(Fore.GREEN, "3 en linea | GANASTE!")
        print(Fore.YELLOW, "+5000 Creditos")
        Creditos=Creditos+5000
        JIK=JIK+1
    
    if tragamonedas==4:
        print(Fore.LIGHTYELLOW_EX, "Saliendo del programa...")
    
    elif Creditos<=0:
        print(Fore.RED,"No tienes suficientes creditos...")
    
    if Creditos<=100:
        print(Fore.CYAN, "FIN DEL JUEGO, TE QUEDASTE SIN CREDITOS")
        time.sleep(1)
        break


print(Fore.YELLOW, "Veamos tus puntos...")

if GIG>1:
    print(Fore.YELLOW, "2 Iguales:", GIG)

if KIK>1:
    print(Fore.YELLOW, "3 Iguales:", KIK)

if JIK>1:
    print(Fore.YELLOW, "3 En linea:", JIK)

print(Fore.GREEN, "------------------")
LOP=(GIG * 50) + ( JIK * 5000 ) + (KIK*1000) 
print(Fore.YELLOW, "Tus puntos:", LOP)

if LOP>5000:
    print(Fore.YELLOW, "Tabla de posiciones")
    print(Fore.CYAN, "1.", nombre, ":",  LOP, "puntos")
    print(Fore.MAGENTA, "2. Mixin : 10000 puntos")

else:
    print(Fore.YELLOW, "Tabla de posiciones")
    print(Fore.MAGENTA, "1. Mixin : 10000 puntos")
    print(Fore.CYAN, "2.", nombre, ":",  LOP, "puntos")   