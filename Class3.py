#if condition
    #Action

click = False #Click = falso
Like = 0 #like = 0
click = True #ahora click es True
if click == True: #si click es igual a True
    Like += 1 # Like incremente en 1
    click = False # ahora click es false
# print (Like)
# print(click)

Temperature = 15
Thermo = 15
print("Thermo:",Thermo)
if Temperature <= 15:
    Thermo += 5
print("Thermo:",Thermo)

if Temperature >= 15:
    Thermo -= 3
print(Thermo)
print("---------------------------------")

Time = "Morning"
Sleepy = False
Pijama = "Unknown"
print("Pijama:",Pijama)
if Time == "Night": #or o and uses
    Pijama = "On"
elif Time == "Morning":
    Pijama = "On"
else:
    Pijama = "Off"

print("Pijama:",Pijama)