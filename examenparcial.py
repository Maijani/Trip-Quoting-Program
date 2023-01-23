def agencia():
    print("Bienvenida")
    print("1) Imprimir informacion de tours")
    print("2) Cotizar viaje")
    print("3) Cotizar viaje premium")
    print("4) Fin Programa")   
    
    
agencia()
opción=int(input("Elige la opción deseada: "))
tour=()
numdepersonas=int(input("Favor de ingresar la cantidad de personas: "))
precio= float ()
precionuevo= float()
total= float(precionuevo+(.16*precio))
e= 'TOUR DE EUROPA'
a= 'TOUR DE AFRICA SAFARI'
s= 'TOUR DE SUDAMERICA'

while opción!=4:
    if opción==1:
       print("Tour--------------Duracion----------PrecioxPersona (SIN IVA)") 
       print("Europa------------15 días-----------2,500 USD")
       print("Africa Safari------7 días-----------8,000 USD")
       print("Sudamerica---------10 días-----------1,900 USD");
    elif opción==2:
       print("Has elegido cotizar viaje")
       e= 'TOUR DE EUROPA'
       a= 'TOUR DE AFRICA SAFARI'
       s= 'TOUR DE SUDAMERICA'
       tour=(input("Favor de ingresar 'e' (Europa), 'a' (Africa Safari) o 's' (Sudamerica): "))
       if tour=='e':
          print("TOUR DE EUROPA- 15 DÍAS-$2500")
          numdepersonas=int(input("Favor de ingresar la cantidad de personas: "))
          if numdepersonas>=10:
               precio= 2500-(0.05*2500)  
          elif numdepersonas>=15:
            precio= 2500-(0.1*2500)  
          elif numdepersonas>=25:
            precio= 2500-(0.1*2500)  
          print(e, "- 15 días-", "=", precio+(.16*precio))
       if tour=='a':
          print("TOUR DE AFRICA SAFARI- 7 DÍAS-$8000")
          numdepersonas=int(input("Favor de ingresar la cantidad de personas: "))
          if numdepersonas>=10:
            precio= 8000-(0.03*8000)  
          elif numdepersonas>=15:
            precio= 8000-(0.07*8000)  
          elif numdepersonas>=25:
            precio= 8000-(0.09*8000)  
          print(a, "- 7 días-", "=",  (precio+ (.16*precio)))
       if tour=='s':
          print("TOUR DE SUDAMERICA- 10 DÍAS-$1900")
          numdepersonas=int(input("Favor de ingresar la cantidad de personas: "))
          if numdepersonas>=10:
            precio= 1900-(0.15*1900)  
          elif numdepersonas>=15:
            precio= 1900-(0.20*1900)  
          elif numdepersonas>=25:
            precio= 1900-(0.25*1900)  
          print(s, "- 10 días-", "=", (precio+(.16*precio)))
          premium=input("Favor de ingresar '3' si quieres premium: ");


    elif opción==3:
        print("Has elegido cotizar viaje premium")
        tour=(input("Favor de ingresar 'e' (Europa), 'a' (Africa Safari) o 's' (Sudamerica): "))
        precio1=2500
        precio2=8000
        precio3=1900
        plandepago=int(input("Favor de ingresar '3', '6', '9' o '12' meses sin intereses "))
        if tour=='e' and numdepersonas>=10:
             precionuevo= precio1+ (0.1*precio1)
             total=precionuevo+(.16*precio1)
        elif tour=='e' and numdepersonas>=15:
             precionuevo= precio1+ (0.07*precio1)
             total=precionuevo+(.16*precio)
        elif tour=='e' and numdepersonas>=25:
            precionuevo= precio1+ (0.03*precio1)
            total=precionuevo+(.16*precio1)
            print(e, "[PREMIUM]- 15 días-", total)
            print("Meses sin interes: ", plandepago)
            print("Pago x mes: ", total/plandepago)
        elif tour=='a' and numdepersonas>=10:
             precionuevo= precio2+ (0.1*precio2)
             total=precionuevo+(.16*precio2)
        elif  tour=='a' and numdepersonas>=15:
             precionuevo= precio2+ (0.04*precio2)
        elif  tour=='a' and numdepersonas>=25:
            precionuevo= precio+ (0.01*precio2)
            total= precionuevo+(.16*precio)
            print(a, "[PREMIUM]- 7 días-", total)
            print("Meses sin interes: ", plandepago)
            print("Pago x mes: ", total/plandepago)
     
        elif  tour=='s' and numdepersonas>=10:
             precionuevo= precio3+ (0.12*precio3)
             total=precionuevo+(.16*precio3)
        elif tour=='s' and numdepersonas>=15:
             precionuevo= precio3+ (0.09*precio3)
             total=precionuevo+(.16*precio3)
        elif  tour=='s' and numdepersonas>=25:
            precionuevo= precio3+ (0.05*precio3)
            total=precionuevo+(.16*precio)
            print(s, "[PREMIUM]- 10 días-", total)
            print("Meses sin interes: ", plandepago)
            print("Pago x mes: ", total/plandepago);

    elif opción==4:
        print("Gracias por usar este servicio");
    else:
        print("Elige una opcion valida")

    print()
    agencia()
    opcion=int(input("Elige una opción: "))
print("Gracias por usar este programa")
