    #dictionaries and sets (diccionarios y conjuntos)

# sets = {"Element1","Element2","Element3"}
# print(sets)
# if "Element2" in sets:
#     print(True)
# else:
#     print(False)


# CountryList = []
# for i in range(5):
#     Country = input("Please enter your Country: ")
#     CountryList.append(Country)

# CountrySet = set(CountryList)
 
# print(CountryList)
# print(CountrySet)


CountryList = []
for i in range(5):
    Country = input("Please enter your Country: ")
    CountryList.append(Country)
CountryDictionary = {}
for pais in CountryList:
    if pais in CountryDictionary:
        CountryDictionary[pais] += 1
    else:
        CountryDictionary[pais] = 1
print(CountryList)
print(CountryDictionary) 


# BlackShoes = {44:1,43:2,42:2,41:4,40:2}
# print(BlackShoes)
# while(True):
#     for i in range(2):   
#         PurchaseSize = int(input("Choose the correct: "))
#         if PurchaseSize < 0:
#             print("No negative")
#             break
#         if BlackShoes[PurchaseSize] > 0:
#             BlackShoes[PurchaseSize] -= 1
#             print(BlackShoes)
#         else:
#             print("No hay stock")
#     break

