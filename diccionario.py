def run():
    mi_diccionario= {
        'llave1' :1,
        'llave2' :2,
        'llave3' :3,        
    }
    print(mi_diccionario['llave2'])
    poblacion_pais={
        'Argentina': 43244,
        'Brazil': 4325345,
        'Chile': 45345,
    }
    for pais in poblacion_pais.keys(): #Se imprimen las llaves
      print(pais)
    for poblacion in poblacion_pais.values(): #Se imprimen los valores de las llaves
       print(poblacion)
    for pais,poblacion in poblacion_pais.items():
         print(pais + ' tiene ' + str(poblacion) + ' habitantes ')
    
    
if __name__ == '__main__':
    run()