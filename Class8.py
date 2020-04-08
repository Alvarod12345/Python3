#making shapes with loops (haciendo formas con bucles)

# length = 10
# for pos in range(1,length+1):
#     print("*"*pos)
#     # print(pos)
# for pos in range(length-1,0,-1):
#     print("*"*pos)

#nested loops (bucles anidados)
# / /   0
#-----  1
# / /   2
#-----  3
# / /   4

#izi mode

# for row in range(5): #0,1,2,3,4
#     if row % 2 == 0:
#         print(" | | ", " | | ")
#     else:
#         print("-----","------")

#hard mode
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
        # print(" | | ")
    else:
        print(" -----")
