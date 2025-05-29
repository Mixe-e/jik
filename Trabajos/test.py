#cada alumno tenga las notas de diferentes asignaturas
#sacar promedio

def promedios():
    global total, promedio
    total=0
    promedio=0

promedios()
try:
    alumnos=int(input("Cantidad de alumnos "))
    for i in range(alumnos):
            notas=int(float(input("Cantidad de notas ")))
            for j in range(notas):
                j=j+1
                print("nota:, ", j)
                Escribirnota=int(input(""))
                total=total+Escribirnota
            promedio=total/j
            print("promedio: ", promedio)
            promedio=0
except Exception:
    print("Solo numeros, no letras")
