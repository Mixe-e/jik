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
Beber="Unboton"
botella=600
sed=True





while botella>=0 and sed:
    Beber=input(Fore.YELLOW, "Tomar agua")
    print(Fore.CYAN, "GLU GLU")
    botella-= random.randint(20,60)
    print("Queda,",botella, Fore. CYAN, "ml")
    resp=input(Fore.YELLOW, "Aun tiene sed?")
    if resp=="no":
        sed=False
    time.sleep(1)
