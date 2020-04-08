#Loops

# word = "Hola"
# letters = []

# for wo in  word:
#     print(wo)
#     if wo == "a":
#         print("detected")
#     letters.append(wo)
# # print(letters)

# number = [1,2,3,4,5]

# for n in number:
#     if n%2 == 1:
#         print(n)

# Numbers =[]
# for num in range(1,10,5): #empieza de 1 hasta 10(9), incrementa de 5 en 5
#     Numbers.append(num)
#     print(num)
# print(Numbers)



name = "alvaro"
letras = []
count = 0
for let in name:
    print(let)
    if "a" in let:
        count +=1
        print("Detected")
        letras.append(let)
        print(letras)
else:
    print("Not")
print(count)
