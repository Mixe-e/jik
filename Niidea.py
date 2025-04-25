
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

##---------------------------------------------------------


# palabra=input("Escribe algo: ")
# caract=0
# for i in palabra:
#     caract=caract+1
# print("La palabra tiene", caract, "caracteres")


##---------------------------------------------------------

num=10
import time
while num<=0:
    print(num)
    time.sleep(1)
    num-=1