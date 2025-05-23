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
    Cartacrupier1=random.randint(1,2,3,4,5,6,7,8,9,10,J,Q,K,A)
    Cartacrupier2=random.randint(1,2,3,4,5,6,7,8,9,10,J,Q,K,A)
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
                print("""Otra mas?
                    1. Si
                    2. Pasar
                    """)
                if total>21 or totalcrupier>total:
                    print("Perdiste")
                else:
                    print("Ganaste")
                    Credito=Credito+apuesta
            else:
                print(Fore.RED, "NO TIENES CREDITOS SUFICIENTES PARA JUGAR")
                    