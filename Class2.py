# def functionName(input):
#     Action
#     return Output

def addOne(Number):
    Output = Number + 1
    return Output
Var1 = 0
Var2 = addOne(Var1)
Var3 = addOne(Var2)
Var4 = addOne(2)
Var5 = addOne(Var2 + 2)
print("AddOne")
print(Var1)
print(Var2)
print(Var3)
print(Var4)
print(Var5)
print("end")
def AddOneAddTwo(NumberOne,NumberTwo):
    Output = NumberOne + 1 # = 2
    # Output acumula
    # Output + NumberTwo + 1
    Output += NumberTwo + 2 # 2 + 2 + 2 = 6
    return Output
suma = AddOneAddTwo(1,2)
print("AddOneAddTwo")
print(suma)

print("--------------------------------")
def printmessage(message, ntimes = 1):
      print(message * ntimes)
printmessage("Hello")
printmessage("Hello", 5)

print("--------------------------------")
