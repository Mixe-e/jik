def tarjeta():
    global deuda, debito
    deuda=100000
    debito=0



print("Tarjeta de credito")


while True:
    op=int(input("Credito"))
    match op:
        case 1:
            print("Pago de la tarjeta de credito")
            print("Deuda:", deuda)
            juk=int(input(""))
            while juk<0 or juk>deuda:
                print("ingrese digito valido")
            print("Descontando deuda...")
            print("-------------------")
            print("Deuda final", deuda=deuda-juk)
        
        case 2:
            print("Compras")
            


















