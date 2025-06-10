
#     -5-4-3 -2 -1
# numeros=[7,5,33,24,9]
#      0,1,2,3,4,5


##print(numeros[0])

#for numero in numeros:
#    print("numero ",numero+1)

# print(numeros)

# numeros.append(64)

# print(numeros)

# ##----------------------

# numeros.insert(3,100)

# print(numeros)


##-------------------------------------------


# frutas=["Manzana", "Mango", "Membrillo"]


##------------------------------------------------


# for fruta in frutas:
#     print(fruta)



# nombres=[]
# apellidos=[]
# while True:

#     print("""
#         1. insertar nombre y apellido
#         2. mostrar nombres y apellidos
#         3. Buscar nombre
#         4. Salir
#         """)


#     op=int(input("Seleccione una opcion "))

#     match op:

#         case 1:
#             nom=input("Ingrese un nombre: ")
#             nombres.append(nom)
#             lil=input("Ingrese un apellido: ")
#             apellidos.append(lil)
        
#         case 2:
#             c=0
#             for n in nombres:
#                 print(nombres[c],apellidos[c])
#                 c=c+1
        
#         case 3:            
#             nom=input("Busca el nombre")       
#             if nom in nombres:
#                 print("El nombre,",nom,"Existe")
#             else:
#                 print("El nombre,", nom,"No existe")
        
#         case 4:    
#             break
        
#         case _:
#             print("Opcion invalida")



##-----------------------------------------------

productos=["Triton", "chocman","pan"]
precio=[800, 300, 1000]
while True:

    lo=int(input("""
                1. Ingresar productos
                2. Comprar
                3. Crear boleta
                4. Salir
                """))
    
    match lo:
        case 1:
            producto=input("Ingresa un numero producto ")
            productos.append(producto)
            precios=input("Ingresa el precio del producto")
            precio.append(precios)
        case 2:
            print("Que vas a comprar?")
            for i in productos:
                c=c+1
                print(i, productos[c], "$",precio[c])
        
        case 3:
            print("Imprimiendo boleta")

            
        case 4:
            break
        case _:
            print("Ingrese una opcion valida")


























































































































































































