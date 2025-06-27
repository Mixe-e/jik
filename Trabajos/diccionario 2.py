personas= {
    1:{"nombre":"daniel", "telefono": 932445769, "rut":2186809890},
    2:{"nombre":"juliana", "telefono": 949537833, "rut":230420556},
}

def registrar():
    persona=str(input("Ingrese nombre"))
    telefono=int(input("Ingrese su numero de telefono:"))
    if len(telefono) !=9:
        print("ERROR")
        return   
    rut=int((input("Ingrese numeros sin punto y guion")))
    sig_id=max(personas.keys()) + 1
    personas[sig_id]={
        "nombre":persona,
        "telefono":telefono,
        "rut":rut
    }
    print("Usuario agregado")


def borrar():
    c=0
    for ids, datos in personas.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")









op=int(input("ola"))
match op:
    case 1:
        registrar()
       
    case 2:   
        borrar()