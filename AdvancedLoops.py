#Advanced Loops

def function(rows,columns):
    for row in range(6): #0,1,2,3,4
        if row % 2 != 0: #0
            for column in range(1,6):
                if column % 2 == 1:
                    if column != 5:
                        print("",end = "")
                    else:
                        print(" ")
                else:
                    print(" |  ",end = "")
                    print("| ",end = "")
                    
            # print(" | | ")
        else:
            print(" -----","----")
    print(" -----","----")
    print("",True)       
function(6,6)