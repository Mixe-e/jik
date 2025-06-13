## Es un conjunto de pares de datos


# dic={
#     "nombre":"Mel Broks",
#     "numero": 945454545,
#     "casado": True,

# }

##  

# print(dic["numero"])


# for key,value in dic.items():
#     print(key, value)

## Agregar cosas al diccionario

# dic["ciudad"]="Talca"

## Comprobando el diccionario con el nuevo dato

# for key,lol in dic.items():
#     print(key, lol)
    
## 

# frutas={

#     "sandia": 3000,
#     "manzanas": 1500,
#     "naranja": 1000,
# }

# print(frutas)
# fruta=input("ingrese una fruta ")
# precio=int(input("Ingrese el precio "))
# frutas[fruta]=precio

##------------------------------------------

frutas={

    "sandia": 3000,
    "manzanas": 1500,
    "naranja": 1000,
}


while True:
    print("""
        1. Ingresar fruta y precios
        2. Actualizar precio
        3. Borrar fruta y precio
        4. Mostrar todas las frutas y precios
        5. Comprar
        6. Salir
        """)

    op=int(input(""))

    match op:
        case 1:
            fruta=input("ingrese una fruta")
            precio=int(input("Ingrese el precio"))
            frutas[fruta]=precio
        
        case 2:
            for key,value in frutas.items():
                print(key, value)
            fruta=input("ingrese una fruta")
            precio=int(input("Ingrese el precio"))
            frutas[fruta]=precio
            

        case 3:
            borrar=int(input("Ingresa la fruta a borrar"))
            frutas.pop(borrar)
        
        case 4:
            print(frutas)
        
        case 5:
            print("Que vas a comprar?")
            for key,value in frutas.items():
                print(key, value)


        case 6:
            break

















