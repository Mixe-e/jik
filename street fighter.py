import random 
randy=random.randint(2,10)
print(randy)
street=50
street2=50
a=0
while street>1 and street2>0:
    if a % 2 == 0:
            print("Ejecutar golpe")
            a=a+1
            randy=random.randint(2,10)
            street=street-randy
            print("Tu golpe hizo", randy)
            print("--------------------")
            print("Vida de street fighter 1: ", street)
    else:
            print("Ejecutar golpe2")
            a=a+1
            randy=random.randint(2,10)
            street2=street2-randy
            print("Tu golpe hizo", randy)
            print("--------------------")
            print("Vida de street fighter 2: ", street2)


if street<1:
    print("Street 2 gana")
else:
    print("Street 1 gana")

            
# input () -> retorna un str ingresado por consola
# nombre = input ("Ingrese su nombre")
# edad=int() -> retorna un integer , str o number
## edad = int("71")
## ** potencia/ elevado a
## % modulo/ MOD 
## / Division
## + Suna
## - Resta
## * Multiplicacion


## Pedir edad
# edad = int(input("Ingrese su edad:"))
# a=float(1)
# print(a)
# if(a<=b):
#     print("a es menor que b")

## cont+=1 <- contador simplificado

## for i in range(10):

