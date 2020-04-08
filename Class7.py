#Class 7
#breaking n continuing in loops

#Participants = ["Alvaro","Sebastian","Johnny","Esmeralda","Dayanna"]
# Position = 1
# for name in Participants:
#     if name == "Esmeralda":
#         break
#     Position += 1
# print(name)
# print(Position)

# #other--------------------------------------------

# for currentIndex in range(len(Participants)):
#     print(currentIndex)
#     if Participants[currentIndex] == "Johnny":
#         print("have a breaked")
#         break
#     print("Not breaked")

# print(currentIndex + 1)

#other--------------------------------------------

for num in range(10):
    if num % 3 == 0:
        print(num)
        print("Its divisible by 3")
        continue
    if num % 4 == 0:
        print(num)
        print("Its divisible by 4")
        continue
    print(num)
    print("Not divisible by 3")

"""
code quiz

Word = "Hello"                       
Letters = []                        
for w in Word:                        
    Letters.append(w)               
print(Letters)   

#another

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1

#another

for i in range(2.0):
    print(i) #error decimal no puede ser interpretado por entero

#another

X = "abcd"
for i in range(len(X)):
    print(i)

"""

