def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 6534:
    #         break
    contador = 0
    texto= (input('Escribe un texto: '))
    while contador < len(texto):
        
        
        if contador == 5:
            break
        else: 
            print(texto[contador])
            contador+= 1
            continue
        
        

if __name__=='__main__':
    run()