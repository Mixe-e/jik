import colorama
from colorama import Fore
import random
import time

def Blackjack():
    global J, Q, K, A
    J=10
    Q=10
    K=10
    A=1
def apuestas():
    global apuesta, Credito, op, total
    apuesta=50
    Credito=100
    op=0
    total=0
def crupier():
    global Cartacrupier1, Cartacrupier2, totalcrupier
    totalcrupier=0
    Cartacrupier1=random.randint(1,13)
    if Cartacrupier1== 11:
        Cartacrupier1=J
    elif Cartacrupier1 == 12:
        Cartacrupier1=Q
    elif Cartacrupier1 == 13:
        Cartacrupier1=K
    elif Cartacrupier1 == 1:
        Cartacrupier1=A
    Cartacrupier2=random.randint(1,13)
    if Cartacrupier2== 11:
        Cartacrupier2=J
    elif Cartacrupier2 == 12:
        Cartacrupier2=Q
    elif Cartacrupier2 == 13:
        Cartacrupier2=K
    elif Cartacrupier2 == 1:
        Cartacrupier2=A    
    totalcrupier=totalcrupier+Cartacrupier1+Cartacrupier2





Blackjack()
apuestas()


while True:
    print("""
    1. Cambiar apuesta
    2. Jugar
    """)
    op=int(input(""))
    match op:
        case 1:
            print(Fore.YELLOW, "Cambia tu apuesta")
            print(Fore.CYAN, """
                1. 50 Creditos
                2. 100 Creditos
                """)
            apostar=int(input(""))
            match apostar:
                case 1:
                    print("Apuesta cambiada a 50 Creditos!")
                    time.sleep(1)
                case 2:
                    print("Apuesta cambiada a 100 Creditos!")
                    time.sleep(1)
        case 2:
            if apuesta<Credito:
                Credito=Credito-apuesta
                Carta1=random.randint(1,10)
                Carta2=random.randint(1,10)
                total=total+Carta1+Carta2
                crupier()
                print(Fore.YELLOW, "Cartas del crupier")
                print(Fore.WHITE, Cartacrupier1, Cartacrupier2)
                print("-------------------------")
                print(Fore.YELLOW, "Tus cartas")
                print(Fore.WHITE, Carta1, Carta2)
                while True:
                    op2=int(input("""Otra mas?
                    1. Si
                    2. Pasar
                    """))
                    match op2:
                        print()
                    if total>21 or totalcrupier>total:
                        print("Perdiste")
                    else:
                        print("Ganaste")
                        Credito=Credito+apuesta
            else:
                print(Fore.RED, "NO TIENES CREDITOS SUFICIENTES PARA JUGAR")
                    