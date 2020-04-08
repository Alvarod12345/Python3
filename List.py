myUniqueList = []
myLeftovers = []
Unique = []  
#funcion añadir con append cada elemento
def add(element): #function
    myUniqueList.append(element) #añade el elemento
    return element #retorna el elemento
#Valores de entrada(input)
add(1)
add(2)
add(1)
#condiciones , conditional
for x in myUniqueList: #para x(valor) en myUniqueList,  
    if x not in Unique: #si x(valor) no esta en la lista Unique 
        Unique.append(x) #lo añade
        print(True,", Se agregó:",x) #imprime
    else: #sino
        if x not in myLeftovers: #si x(valor) no esta en myLeftovers
            myLeftovers.append(x) #lo añade
            print(False,", No se agregó",x) #imprime
print(myUniqueList)
print("Unique:",Unique)
print("Reps:",myLeftovers)


