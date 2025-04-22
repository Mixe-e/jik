

# # Ingreso de variables

# print("ingrese su nombre")
# nombre=input()
# print("ingrese su edad")
# edad=input()

# print("holaaaa ,",nombre, "y su edad es", edad)

# # Suma

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# print(n1+n2)

# # Multiplicacion

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# print("La multiplacion de estos numeros da", n1*n2)


# # Promedio de 3 numeros

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# n3=int(input("ingrese un numero "))
# n4=n1+n2+n3

# if n4>=40:
    # print("el alumno aprobo")
# else:
    # print("el alumno reprobo")

# print("El promedio es", n4/3)

## Edad ingresar 

# edad=int(input("ingrese su edad"))
# if edad>=18:
    # print("usted es mayor de edad")

# elif edad>=12 and edad=<18:
    # print("Usted es adolescente")
# elif edad>=18 and edad=<65:
    # print("Usted es un adulto")
# else edad>65
    # print("Usted es un viejo")





# # Inicio de tabla de multiplicar

# cant=int(input("ingrese la cantidad de repeticiones "))
# for i in range(cant):
    # print("Esta es la table del ", i)
    # for j in range(1,10):
        # print(i, "*", j, "=", i*j)


# # Fin Para

# nombre=input("ingrese su nombre")
# edad=input("ingrese su edad")
# print("hola", nombre, "su edad es", edad)


# num=int(input("ingrese un numero"))

# # Sacar promedio definido por el usuario

#cant=int(input("ingrese la cantidad de notas"))
#total=0
#notasazules=0
#for i in range(cant):
#    print("ingrese la nota", i+1)
#    nota=float(input(""))
#    total=total+nota
#    if nota>=4:
#        notasazules=notasazules+1
#promedio=total/cant
#print("el promedio es", promedio)
#print("la cantidad de notas azules son:", notasazules)
#if promedio>=4:
#    print("el alumno aprobo")
#else:
#    print("el alumno reprobo")


## Clave wegfweg

# clave=1234
# y=3
# for i in range(3):
#     pas=int(input("ingrese la clave"))
    
#     if clave==pas:
#             print("blenvenido al sistema")
#             break
#     else:
#         y=y-1
#         print("clave incorrecta, quedan", y , "intentos")

 # Equivalent of "según" (according to) in PSeInt using if-elif-else in Python


total = 0
palta=3000
tomate=2000
naranja=1500
pera=300
Ak47=100000

while True:
    print("1. Palta")
    print("2. Tomate")
    print("3. Naranja")
    print("4. Pera")
    print("5. Ak-47")
    print("6. Salir")
    opcion = int(input("Ingrese una opción (1-5): "))

    if opcion == 1:
        print("Llevaste 1 palta")
        total=total+palta
    elif opcion == 2:
        print("Llevaste 1 tomate")
        total=total+tomate
    elif opcion == 3:
        print("Llevaste 1 naranja")
        total=total+naranja
    elif opcion == 4:
        print("Llevaste 1 pera")
        total=total+pera
    elif opcion == 5:
        print("Llevaste 1 Ak-47")
        total=total+Ak47
    elif opcion == 6:
        break
    else:
        print("Opción no válida")
    opcion = int(input("Ingrese una opción (1-6): "))


print("total de palta:", palta)
print("total de tomate:", tomate)
print("total de naranja:", naranja)
print("total de pera:", pera)
print("total de Ak-47:", Ak47)
print("El total es:", total)
print("Gracias por su compra")