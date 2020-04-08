#Tic Tac Toe, Part A

def drawField(field):
    for row in range(5):
        if row % 2 == 0:
            practicalRow = int(row / 2)
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = int(column / 2)
                    if column != 4:
                        print(field[practicalColumn][practicalRow],end = "")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|",end = "")
        else:
            print("-----")

Player = 1
currentField = [[" "," "," "],[" "," "," "],[" "," "," "]]  #element1,element2,element3
drawField(currentField) 
while(True):
    print("Player turn: ",Player)
    MoveRow = int(input("Please enter the row:\n"))
    MoveColumn = int(input("Please enter the column:\n"))
    if Player == 1:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            Player = 2
    else:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1
    drawField(currentField)    

