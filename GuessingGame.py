# Part A
# from random import randint

# randVal = randint(1,100)
# while(True):    # while(True==True):
#     guess = int(input("Input a number: "))
#     if guess == randVal:
#         print("Ganaste")
#         break
#     elif guess < randVal:
#         print("Tu numero debe ser mas alto")
#     else:
#         print("Tu numero debe ser mas bajo")
# print("La respuesta correcta es: ", randVal)



# Part B
from random import random
from time import clock

randVal = random()
print(randVal)

upper = 1.0
lower = 0.0
guess = 0.5
startTime = clock()
while(True):
    guess = (lower + upper) / 2
    if guess == randVal:
        break
    elif guess < randVal:
        lower = guess
    else:
        upper = guess
endTime = clock()
print(guess)
print("Tomó: ",endTime-startTime," seconds")

    
