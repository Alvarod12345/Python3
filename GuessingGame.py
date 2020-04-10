from random import randint

randVal = randint(1,100)
while(True):    # while(True==True):
    guess = int(input("Input a number: "))
    if guess == randVal:
        print("Ganaste")
        break
    elif guess < randVal:
        print("Tu numero debe ser mas alto")
    else:
        print("Tu numero debe ser mas bajo")
print("La respuesta correcta es: ", randVal)