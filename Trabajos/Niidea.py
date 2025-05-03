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

# num=0
# import time
# while num<=3123214151512510:
#     print(num)
#     time.sleep(0)
#     num+=1

##---------------------------------------------------------

# resp="no"

# while resp!="si":
#     resp=input("Desea salirse del programa?")

##--clave--------------------------------------------------

# clave=3239
# intentos=3
# contraseña=int(input("ingrese contraseña"))

# while clave!=contraseña :
#     print("error contraseña invalida")
#     print("Quedan", intentos, "intentos")
#     contraseña=int(input("ingrese contraseña"))
#     if intentos==1:
#         break

# if clave==contraseña:
#     print(" Clave aceptada")
# else:
#     print("acceso denegado")

##------------------------------------------------------------


# numero=(int(input("Ingrese un numero")))
# if numero % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")



##------------------------------------------------------------

uet="s"
total=0
total2=0

print("Nota: escriba el ", uet, " para salir")
numero2=(int(input("Contador de numeros")))

while numero2!= uet:   
        numero2=(int(input("agrega otro numero, escribe ", uet, " para salir")))
        total2=total2+1
        total=total+numero2
        if uet == "s":
            break

print("La suma total es:", total)
print("Tus numeros ingresados fueron", total2)



