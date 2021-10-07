listaPrueba=[True,False, 'Mente', 1,5,2,False]
listaPrueba.append('Noviembre') #agregar
listaPrueba.pop(1) #remove
print(listaPrueba)

for elemento in listaPrueba:
    print(elemento)

listaPrueba= listaPrueba[::-1] #Invertir la lista
print(listaPrueba)