# Crear gestion de vehiculos
# Crear programa para un parking de autos
# se debe ingresar
# Marca, año, patente, Tipo

# Marca: tipo string, se debe tipear la marca
# año: tipo int , solo de 4 digitos enteros
# patente: debe tener 4 letras minusculas y 2 digitos
# tipo: S= sedan, C= Camioneta, M= moto

# Se deve validar cada aspecto y tener un mantenedor para 
# todos los vehiculos motorizados

# 1.- Ingresar Vehiculo
# 2.- Mostrar Vehiculos
# 3.- Actualizar Vehiculo
# 4.- Borrar Vehiculo
# 5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
# 6.- Salir

# Usar dunciones con argumentos para poder validar
# y para poder llamar las acciones dentro del menu

Parking={
    "Marca":["Ford"],
    "Año":["1994"],
    "Patente":["BXFD10"],
    "Tipo":["S"],
}


while True:
    eleccion=int(input("""Parking de autos
            1.Ingresar vehiculo
            2.Mostrar vehiculos
            3.Actualizar vehiculo
            4.Borrar vehiculo
            5.Mostrar estadisticas
            """))
    match eleccion:
        case 1:
            marca=input("Coloca la marca")
            año=input("Coloca el año")
            patente=input("Coloca la patente")
            tipo=input("Coloca el tipo")

            Parking["Marca"].append(marca)
            Parking["Año"].append(año)
            Parking["Patente"].append(patente)
            Parking["Tipo"].append(tipo)
        case 2:
            print("Lista de vehiculos")
            for i in range(len(Parking["Marca"])):
                print(f" {i+1}. Marca: {Parking['Marca'][i]}, Año: {Parking['Año'][i]}, Patente: {Parking['Patente'][i]}, Tipo: {Parking['Tipo'][i]}")
        case 3:
            print("")

        case 4:
            for i in range(len(Parking["Marca"])):
                print(f" {i+1}. Marca: {Parking['Marca'][i]}")
                borrar=int(input("Cual auto vas a borrar?"))
                borrar=borrar-1
                Parking["Marca"].pop(borrar)
                Parking["Año"].pop(borrar)
                Parking["Patente"].pop(borrar)
                Parking["Tipo"].pop(borrar)
        case 5:
            print("Saliendo")
            break
        
        case _:
            print=("Ingrese un numero valido")
