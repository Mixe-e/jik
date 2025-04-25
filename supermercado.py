print("bienvenido al supermercado")
jugo=10
ak=5
pistola=1

escritura = input
usuario= input
total=0


while usuario!=4:
    print("Que va a llevar?")
    print("1.ak")
    print("2.pistola")
    print("3.jugo de manzana")
    print(input(escritura))
    if escritura==3:
        print("te has llevado una ak")
        total=total+ak
    elif escritura==2:
        print("te llevaste una pistola")
        total=total+pistola
    elif escritura==1:
        print("te llevaste un jugo de manzana")
        total=total+jugo
    else:
        print("Di algo valido")

print("Gracias por comprar, el recibo:")
print("Pistola: ", pistola)
print("ak: ", ak)
print("jugo: ", jugo)
print("Total: ", total)
