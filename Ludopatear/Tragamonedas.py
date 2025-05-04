import colorama
import random
import os
import time

from colorama import init, Fore, Back, Style
lanzando=8
Creditos=1000
tragamonedas="unboton"



while tragamonedas != 4:
    print("Tus creditos:",Fore.YELLOW, Creditos)
    print("----------------------------------------")
    tragamonedas=(input("Pulsa cualquier boton para tirar..."))
    if Creditos>=100:  
        Creditos=Creditos-100
        Slot1=random.randint(1,5)
        print(Slot1)
        time.sleep(0.10)
        Slot2=random.randint(1,5)
        print(Slot2)
        time.sleep(0.10)
        Slot3=random.randint(1,5)
        print(Slot3)
        time.sleep(0.10)
    if Slot1==Slot2==Slot3:
        print(Fore.GREEN, "3 Iguales | GANASTE!")
        print(Fore.YELLOW, "+1000 Creditos")
        Creditos=Creditos+1000
    if Slot1==Slot2 or Slot2==Slot3 or Slot1==Slot3:
        print(Fore.GREEN, "2 Iguales | GANASTE!")
        print(Fore.YELLOW, "+50 Creditos")
        Creditos=Creditos+50
    if Slot1==1 and Slot2==2 and Slot3==3 or Slot1==4 and Slot2==5 and Slot3==6 or Slot1==7 and Slot2==8 and Slot3==9:
        print(Fore.GREEN, "3 en linea | GANASTE!")
        print(Fore.YELLOW, "+5000 Creditos")
        Creditos=Creditos+5000
    
    if tragamonedas==4:
        print(Fore.LIGHTYELLOW_EX, "Saliendo del programa...")
    
    elif Creditos<=0:
        print(Fore.RED,"No tienes suficientes creditos...")