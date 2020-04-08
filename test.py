"""
la primera pasada dandole el valor 0 se vuelve 1, 
la segunda pasada que es 1 se incrementa mas 1 y imprime 2
"""
# def addOne(number):
#        number += 1
#        return number
# one = addOne(0)
# two = addOne(one)
# print(two)


#en este codigo falta llamar a la funcion y no a la salida(output)
# def sumA(count):
#      a = count+1
#      return a
# # print(a)

# li=[["john","doe"]]
# # print(li[-1][-1])

"""
funka

myUniqueList = []
myLeftovers = []
unicos = []  

def add(element):
    myUniqueList.append(element)
    return element
add(1)
add(2)
add(1)


for x in myUniqueList:
    if x not in unicos:
        unicos.append(x)
        print(True,", Se agregó:",x)
    else:
        if x not in myLeftovers:   
            myLeftovers.append(x)
            print(False,", No se agregó",x)
print("Unicos:",unicos)
print("Repetidos:",myLeftovers)
"""

# nombres = ["Johnny","Esmeralda","Dayanna","Alvaro","Sebastian"]
# edades = [45,46,23,21,13]
# familia =[["Johnny",45],
#           ["Esmeralda",46],
#           ["Dayanna",23],
#           ["Alvaro",21],
#           ["Sebastian",13]]

# familia.append(["Rosa",22])

# # print(familia)
# for famili in familia:
#     print("{:9}: {:2}".format(famili[0],famili[1]))  

#another-code-abt-prime

# def esPrimo(n):
#     if n<2:
#         return False
#     for x in range(2,n):
#         if n % x == 0:
#             return False
#         return True
# def SeriePrimo(numPrimo):
#     c = 0
#     i = 0
#     while c < numPrimo:
#         i += 1
#         if esPrimo(i):
#             c += 1
#             print(i)
# SeriePrimo(10)

# def primo():
#     num1 = 3
#     num2 = 100
#     for x in range(num1,num2):
#         if (num2 % x)==0:
#         # es divisible
#             return False
#     return True
#end



# Length = 3
# for pos in range(1, 3):    
#     print("c"*pos)

# x = 2
# for i in range(x):
#       for j in range(x):
#         a = x - j + i
#         print(a)

# f = 1
# A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# for i in range(0, 3):
#      f =f*i
#      for j in range(0, 3):
#          A[i][j] = f
# print(A)


#dictionary 
# nums = set([7,7,1,3,4,5,5,2]) #imprime 6 no cuenta las repeticiones
# # print(len(nums))

# dict = {}
# dict[1] = 2
# dict['1'] = 4
# dict[1] += 2
# count = 0

# for key in dict:
#     count += dict[key]

# print(count)


#file I/O

# VacationSpots = ["Trujillo","Chimbote","Tumbes","Arequipa"]
# VacationFile = open("Lugares","w")
# for x in VacationSpots:
#     VacationFile.write(x + "\n")
# VacationFile.close()
# VacationFile = open("Lugares","r")
# first = VacationFile.readline()
# print(first)
# second = VacationFile.readline()
# print(second)
# third = VacationFile.readline()
# print(third)
# fourth = VacationFile.readline()
# print(fourth)
# for line in VacationFile:
#     print(line,end = "")
# VacationFile.close()

# FinalSpot = "Piura"
# VacationFile = open("Lugares","a")
# VacationFile.write(FinalSpot)
# VacationFile.close()

# VacationFile = open("Lugares","r")
# for x in VacationFile:
#     print(x,end = "\n")
# VacationFile.close()




# #project 1 
# # example 1
# def play(n=None):
#     if n is None:
#         while True:
#             try:
#                 n = int(input('Input the grid size: '))
#             except ValueError:
#                 print('Invalid input')
#                 continue
#             if n <= 0:
#                 print('Invalid input')
#                 continue
#             break

#     grids = [[0]*n for x in range(n)]
#     user = 1
#     print('Current board:')
#     print(*grids, sep='\n')
#     while True:
#         user_input = get_input(user, grids, n)
#         place_piece(user_input, user, grids)
#         print('Current board:')
#         print(*grids, sep='\n')

#         if (check_won(grids, user, n) or
#                 check_won(zip(*grids), user, n) or
#                 diagcheck_won(grids, user, n) or
#                 diagcheck_won(grids[::-1], user, n)):
#             print('Player', user, 'has won')
#             return

#         if not any(0 in grid for grid in grids):
#             return

#         user = 2 if user == 1 else 1
# def get_input(user, grids, n):
#     instr = 'Input a slot player {0} from 1 to {1}: '.format(user, n)
#     while True:
#         try:
#             user_input = int(input(instr))
#         except ValueError:
#             print('invalid input:', user_input)
#             continue
#         if 0 > user_input or user_input > n+1:
#             print('invalid input:', user_input)
#         elif grids[0][user_input-1] != 0:
#             print('slot', user_input, 'is full try again')
#         else:
#             return user_input-1


# def place_piece(user_input, user, grids):
#     for grid in grids[::-1]:
#         if not grid[user_input]:
#             grid[user_input] = user
#             return


# def check_won(grids, user, n):
#     return any(all(cell == user for cell in grid) for grid in grids)


# def diagcheck_won(grids, user, n):
#     return all(grids[x][x] == user for x in range(n))


# if __name__ == '__main__':
#     play()


# example 1

class Team:
    def __init__(self,NombreTeam,CantidadIntegrantes):
        self.Nombre_del_Team = NombreTeam
        self.Cantidad_de_integrante_del_Team = CantidadIntegrantes
    def Asigna_Nombre_Team(self,NombreTeam):
        self.Nombre_del_Team = NombreTeam
    def Cantidad_Integrantes(self,CantidadIntegrantes):        
        self.Cantidad_de_integrante_del_Team = CantidadIntegrantes

# Team1 = Team("Tim","2")
# print(Team1.Nombre_del_Team)
# print(Team1.Cantidad_de_integrante_del_Team)

# #asignamos un nombre
# Team1.Asigna_Nombre_Team("Team Tim 2.0")
# print(Team1.Nombre_del_Team)
# Team1.Cantidad_Integrantes(4)
# print(Team1.Cantidad_de_integrante_del_Team)

# class player(Team):
#     def __init__(self, PName,PSchool,Nombre_del_Team, Cantidad_de_integrante_del_Team):
#         Team.__init__(self,Nombre_del_Team,Cantidad_de_integrante_del_Team)
#         self.playerName = PName
#         self.PlayerSchool = PSchool
    
#     def setName(self,name):
#         self.playerName = name
#     def setPSchool(self,school):
#         self.PlayerSchool = school
#     def CantIntegrantes(self):
#         self.Cantidad_de_integrante_del_Team += 1
#     def __str__(self):
#         return ("Hay "+ str(self.Cantidad_Integrantes)+" integrantes")
    
# Player1 = player("Alvaro","URP","Dinamita's Team",0)
# Player1.CantIntegrantes()
# print(Player1.playerName)
# print(Player1.PlayerSchool)
# print(Player1.Nombre_del_Team)
# print(Player1.Cantidad_de_integrante_del_Team)



# example 2
# class Merch:
#     def __init__(self,q,d):
#         self.Quality = q
#         self.Delivery = d

#     # getters
#     def getQuality(self):
#         return self.Quality
#     def getDelivery(self):
#         return self.Delivery

#     # setters
#     def setQuality(self,quality):
#         self.Quality = quality
#     def setDelivery(self,delivery):
#         self.Delivery = delivery

# class Brand(Merch):
#     def __init__(self, n, c, quality, delivery):
#         Merch.__init__(self,quality,delivery)
#         self.NameBrand = n
#         self.Cuantity = c
#     # def NameB(self):
#     #     return self.NameBrand
#     # def Cuant(self):
#     #     return self.Cuantity

# Brand1 = Brand("Wors",20,"Very High",True)
# print(Brand1.NameBrand)
# print(Brand1.Cuantity)
# print(Brand1.Quality)
# print(Brand1.Delivery)

class Cat:
    def __init__(self,name="Cat"):
        self.name = name
        self.breed = breed

myCat = Cat("Mia")