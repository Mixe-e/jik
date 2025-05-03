
import colorama
import time

from colorama import init, Fore, Back, Style
lil="weoifgheworgeogije"
print(Fore.LIGHTYELLOW_EX, "Bienvenido al puteador de pilous")
print(Fore.LIGHTYELLOW_EX, "AHORA EN PYTHON!")
puteador=0
PilouP=0
PilouW=0
PilouSA=0
PilouTON=0
PilouCTM=0
PilouPE=0

while puteador!=lil:
    
    print(Fore.LIGHTGREEN_EX, """
      Como deseas putear al pilou?
    
        1. Pilou puto
        2. Pilou weon
        3. Pilou saco wea
        4. Pilou tonto
        5. Pilou conchetumare
        6. Pilou pelotudo          
        7. Salir
            """)
    
    puteador=(int(input("")))

    if puteador==1:
        print(Fore.CYAN, "Pilou puto")
        PilouP=PilouP+1
        
    if puteador==2:
        print(Fore.CYAN, "Pilou weon")
        PilouW=PilouW+1
    
    if puteador==3:
        print(Fore.CYAN, "Pilou saco wea")
        PilouSA=PilouSA+1
    
    if puteador==4:
        print(Fore.CYAN, "Pilou tonto")
        PilouTON=PilouTON+1
                       
    if puteador==5:
        print(Fore.CYAN, "Pilou conchetumare")
        PilouCTM=PilouCTM+1

    if puteador==6:
        print(Fore.CYAN, "Pilou pelotudo")
        PilouPE=PilouPE+1

    if puteador==7:
        print(Fore.LIGHTWHITE_EX, "Saliendo del programa...")
        time.sleep(1)
        break

    if puteador>=8:
        print("Selecciona una opcion valida")
        time.sleep(1)



print(Fore.YELLOW, "Terminaste de putearlo?, veamos tus resultados...")

if PilouP>0:
    print(Fore.WHITE, "Veces que le dijiste pelotudo", PilouP)

if PilouW>0:
    print(Fore.WHITE, "Veces que le dijiste weon", PilouW)

if PilouSA>0:
    print(Fore.WHITE, "Veces que le dijiste saco wea", PilouSA)

if PilouTON>0:
    print(Fore.WHITE, "Veces que le dijiste tonto", PilouTON)

if PilouCTM>0:
    print(Fore.WHITE, "Veces que le dijiste conchetumare", PilouCTM)

if PilouPE>0:
    print(Fore.WHITE, "Veces que le dijiste pelotudo", PilouPE)


print(Fore.GREEN, "---------------------------------")
print(Fore.GREEN, "Este puteador fue creado gracias a mise y su afan de putear a pilou cada vez que trolea una ronda en counter straik ")