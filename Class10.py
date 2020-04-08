#I/O

# name = input("Please enter your name: ")
# print("hi",name)

# age = int(input("Enter your age: "))
# print(age)

# age = input("Enter your age: ")
# print(int(age))

# age = int(input("enter ur age: "))
# print(str(age)+"xd")

scores = []
for i in range(3):
    currentScores = float(input("Enter the score "+ str(i+1)+":"))
    #currentScores = input("Enter the score "+ str(i) +":")
    scores.append(currentScores)
print(scores)
