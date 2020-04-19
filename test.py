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

# class Cat:
#     def __init__(self,name="Cat"):
#         self.name = name
#         self.breed = breed

# myCat = Cat("Mia")











import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]

    for line in welcome:
        print(line, sep='\n')

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "billionare", "shampoo"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: # check valid input
                print("That is not valid input. Please try again.")
                continue                
            else: 
                if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: # check the input is only one letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()  






# example2

# from termcolor import colored

# """This is the connect 4 game.
# The player choosing the column on the playing board.
# The player's piece is dropped from the top into grid.
# The pieces fall straight down.
# The piece occupying the lowest available space within the column
# After that turn is passed to the next player.
# The first player formed vertical, horizontal or diagonal line of pieces wins.
# """


# ROW_COUNT = 6
# COLUMN_COUNT = 7

# NO_PIECE = '[ ]'
# PIECE_ONE = colored('[' + u"\u25EF" + ']', color='red', attrs=['bold'])
# PIECE_TWO = colored('[' + u"\u25EF" + ']', color='blue', attrs=['bold'])


# def new_board(board):
#     """Function creates new board by making list of lists
#     Arguments:
#         board {list} -- empty list
#     Returns:
#         [list] -- list filled with NO_PIECE to create "empty" playing board
#     """
#     for dummy in range(ROW_COUNT):
#         board.append([NO_PIECE]*COLUMN_COUNT)
#     return board


# def draw_board(board):
#     """Function drawing playing board with individual NO_PIECE elements
#     Arguments:
#         board {list} -- list of lists filled with NO_PIECE elements
#     """
#     for row in reversed(board):
#         for element in range(len(row)):
#             if element != len(row)-1:
#                 print(row[element], end="")
#             else:
#                 print(row[element])


# def is_location_valid_for_turn(board, col):
#     """Function checking if chosen spot for turn has NO_PIECE in it
#     Arguments:
#         board {list} -- playing board
#         col {int} -- the number of chosen column for the turn
#     Returns:
#         boolean -- True if spot is vaild for turn, False otherwise
#     """
#     try:
#         return board[ROW_COUNT-1][col] == NO_PIECE
#     except IndexError:
#         print(colored('You must choose the number of columnt between 1 and ' +
#               str(COLUMN_COUNT), 'white', 'on_red', attrs=['bold']))


# def make_move(board, row, col, piece):
#     """Function is placing the piece of a player into chosen spot
#     Arguments:
#         board {list} -- playing board
#         row {int} -- row of the playing board
#         col {int} -- column of the playing board
#         piece {str} -- the piece symbol, depends on the player
#     """
#     board[row][col] = piece


# def get_next_free_row(board, col):
#     """The function chosing the row with NO_PIECE element
#     after player chose column for turn
#     Arguments:
#         board {list} -- playing board
#         col {int} -- chosen column
#     Returns:
#         int -- the row number of the free row
#     """
#     for r in range(ROW_COUNT):
#         if board[r][col] == NO_PIECE:
#             return r


# def winning_move(board, piece):
#     """Function checking after the player's move was winning.
#     Function scan playing board.
#     If there is 4 same pieces are placed in 3 types of line.
#     Types of lines: horizontal, vertical, diagonal.
#     If it found 4 pieces then player who's piece is it won.
#     There 4 for loops for each case.
#     TODO: optimize searching for winning move
#     Arguments:
#         board {list} -- playing board
#         piece {str} -- the piece symbol depends on the player
#     Returns:
#         boolean -- True if move was winning
#     """
# # Horizontal
#     for c in range(COLUMN_COUNT-3):
#         for r in range(ROW_COUNT):
#             if board[r][c] \
#                     == board[r][c+1] \
#                     == board[r][c+2] \
#                     == board[r][c+3] \
#                     == piece:
#                 return True
# # Vertical
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT-3):
#             if board[r][c] \
#                     == board[r+1][c] \
#                     == board[r+2][c] \
#                     == board[r+3][c] \
#                     == piece:
#                 return True
# # Positive diagonal
#     for c in range(COLUMN_COUNT-3):
#         for r in range(ROW_COUNT-3):
#             if board[r][c] \
#                     == board[r+1][c+1] \
#                     == board[r+2][c+2] \
#                     == board[r+3][c+3] \
#                     == piece:
#                 return True
# # Negative diagonal
#     for c in range(COLUMN_COUNT-3):
#         for r in range(3, ROW_COUNT):
#             if board[r][c] \
#                     == board[r-1][c+1] \
#                     == board[r-2][c+2] \
#                     == board[r-3][c+3] \
#                     == piece:
#                 return True


# def main():
#     """The function creating and drawing playing board.
#     After that in while loop changing playing turns.
#     For each player turn calls functions to:
#     check location, get next free row and check for win move.
#     If someone wins printing winner message.
#     """
#     board = []
#     board = new_board(board)
#     draw_board(board)
#     game_over = False
#     turn = 0

#     while not game_over:

#         if turn == 0:
#             col = int(input('Player 1 making turn(1-7): '))
#             col_number = col - 1

#             if is_location_valid_for_turn(board, col_number):
#                 row = get_next_free_row(board, col_number)
#                 make_move(board, row, col_number, PIECE_ONE)
#                 if winning_move(board, PIECE_ONE):
#                     print(colored('PLAYER 1 WINS!', 'red', attrs=['bold']))
#                     game_over = True

#         else:
#             col = int(input('Player 2 making turn(1-7): '))
#             col_number = col - 1

#             if is_location_valid_for_turn(board, col_number):
#                 row = get_next_free_row(board, col_number)
#                 make_move(board, row, col_number, PIECE_TWO)
#                 if winning_move(board, PIECE_TWO):
#                     print(colored('PLAYER 2 WINS!', 'blue', attrs=['bold']))
#                     game_over = True

#         turn += 1
#         turn = turn % 2
#         draw_board(board)


# main()