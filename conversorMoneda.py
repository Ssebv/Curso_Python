menu= """
BIENVENDO al conversor de monedas clp a ... 💵

1 - Dollares
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion para realizar la convercion:  """

opcion= input(menu)
if opcion == '1':
    pesos= float(input('Ingrese sus pesos chilenos a convertir: '))
    valor= float(785.56)

    total= (pesos / valor)
    total =round(total,2)# redondear decimales
    total= str(total)
    
elif opcion == '2':
    pesos= float(input('Ingrese sus pesos chilenos a convertir: '))
    valor= float(8.5)

    total= (pesos / valor)
    total =round(total,2)# redondear decimales
    total= str(total)

elif opcion == '3':
    pesos= float(input('Ingrese sus pesos chilenos a convertir: '))
    valor= float(38.98)

    total= (pesos / valor)
    total =round(total,2)# redondear decimales
    total= str(total)

  
else:
    print('Ingrese una opcion correcta porfavor')



print('Tienes $' + total )

