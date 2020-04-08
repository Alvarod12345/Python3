#TAREA 3
#"If" Statements
def function(var1,var2,var3):
    if var1 == var2 or var1 == var3 or var2 == var3:
        print(True)
    else:
        print(False)

function(2,1,1)
    
print("------------Same-------------") 

def function2(var1,var2,var3):
    if int(var1) == int(var2):
        print(True)
    elif int(var1) == int(var3):
        print(True)
    elif int(var2) == int(var3):
        print(True)
    else:
        print(False)
function2("3","2","2")


