import colorama
import random
import time
import os
from colorama import init, Fore, Back, Style
anticheat="wripgpweriobjerstpobsertjiopbsertpiojbdertopjbrtopibjrtiopbhnrtbhrtopijbhdft"
continuar="un boton"
creditos=1000
ruleta=999
apostar= 0
n= 0
v= 0
r= 0
lanzando=8

print(Fore.CYAN, "Bienvenido al casino,",Fore.YELLOW,"AHORA EN PYTHON!")
while apostar != anticheat:
    
    print(Fore.YELLOW, "Tienes:", creditos)
    print(Fore.YELLOW, "Donde quieres apostar?")
    print(Fore.BLUE, "-----------------------------")
    print(Fore.GREEN, "1. 100 al verde")
    print(Fore.RED, "2. 100 al rojo")
    print(Fore.BLUE, "3. 100 al negro")
    print(Fore.YELLOW, "4. Como jugar?")
    print(Fore.YELLOW, "5.Salir del casino")
    apostar=(int(input("")))
    if apostar==1:
        if creditos>=100:         
            v=v+100
            creditos=creditos-100
            print(Fore.WHITE, "Lanzando ruleta...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            ruleta=random.randint(0,36)
            print(ruleta)
            time.sleep(1)
            for i in range(lanzando):
                os.system('cls' if os.name == 'nt' else 'clear')
                ruleta=random.randint(0,36)
                print(ruleta)
                time.sleep(0.05)

            if ruleta==0:
                print(Fore.GREEN, "GANASTE!")
                print(Fore.YELLOW, "+1400 C")
                creditos=creditos+1400
            else:
                print(Fore.RED, "Perdiste")
        else:
            print(Fore.RED, "Necesitas mas dinero...")
    
    if apostar==2:
        if creditos>=100: 
            r=r+100
            creditos=creditos-100
            print(Fore.WHITE, "Lanzando ruleta...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            ruleta=random.randint(0,36)
            print(ruleta)
            time.sleep(1)
            for i in range(lanzando):
                os.system('cls' if os.name == 'nt' else 'clear')
                ruleta=random.randint(0,36)
                print(ruleta)
                time.sleep(0.05)

            if ruleta % 2 != 0:
                print(Fore.GREEN, "GANASTE!")
                print(Fore.YELLOW, "+200 C")
                creditos=creditos+200 
            else:
                print(Fore.RED, "Perdiste")
        else:
            print(Fore.RED, "Necesitas mas dinero...")

    if apostar==3:
        if creditos>=100:                
            n=n+100
            creditos=creditos-100
            print(Fore.WHITE, "Lanzando ruleta...")
            time.sleep(1)
            for i in range(lanzando):
                os.system('cls' if os.name == 'nt' else 'clear')
                ruleta=random.randint(0,36)
                print(ruleta)
                time.sleep(0.05)

            if ruleta % 2 == 0:
                print(Fore.GREEN, "GANASTE!")
                print(Fore.YELLOW, "+200 C")
                creditos=creditos+200 
            else:
                print(Fore.RED, "Perdiste")
        else:
            print(Fore.RED, "Necesitas mas dinero...")  
    
    if apostar==4:
        print(Fore.YELLOW, """Como jugar?
              1. Apostar al verde es apostarle al 0
              2. Apostar al rojo es apostarle aquellos numeros impares
              3. Apostar al negro es apostarle aquellos numeros pares             
              """)
        continuar=(input("Pulse cualquier boton para continuar..."))

    if apostar==5:
        print(Fore.YELLOW, "Saliendo del casino...")
        time.sleep(1)
        break
    
    elif apostar>=6:
        print(Fore.WHITE, "Selecciona un numero valido")
        time.sleep(1)



print(Fore.YELLOW, "Terminaste de ludopatear?, veamos tus resultados...")
print(Fore.GREEN, "Dinero gastado en apostarle al verde:", Fore.YELLOW, v)
print(Fore.RED, "Dinero gastado en apostarle al rojo:", Fore.YELLOW, r)
print(Fore.BLUE, "Dinero gastado en apostarle al negro:", Fore.YELLOW, n)
print(Fore.YELLOW, "Tu dinero final:", creditos)