#Participant Data a,b,c

# ParticipantNumber = 5
# participantData = []
# registeredParticipants = 0
# outputFile = open("Participants.txt","w")
# while(registeredParticipants < ParticipantNumber):
#     tempPartData = [] #name, country, age
#     name = input("Please enter your Name: ")
#     tempPartData.append(name)
#     country = input("Please enter your Country: ")
#     tempPartData.append(country)
#     age = int(input("Please enter your Age: "))
#     tempPartData.append(age) #[name,country,age]
#     print("temporaly data",tempPartData)
#     participantData.append(tempPartData) #   [participantData] = [tempPartData]= [name,country,age]
#     registeredParticipants +=1 #registeredParticipants + 1
# print("participant Data",participantData)

# for participant in participantData:
#     for data in participant:
#         outputFile.write(str(data))
#         outputFile.write(" ")
#     outputFile.write("\n")       

# outputFile.close()

inputFile = open("Participants.txt","r")
inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split() 
    print("tempparticipante",tempParticipant)
    inputList.append(tempParticipant)
    print("inputlist",inputList)
    # "Max Peru 21 \n".strip("\n") -> "Max Peru 21 "
    # "Max Peru 21 ".split() -> ["Max","Peru","21"]
Age = {}
print(inputList)
for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1            
print(Age)

Oldest = 0
Youngest = 100
counter = 0
mostOcurringAge = 0
for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge 
    if Age[tempAge]>=counter:
        counter = Age[tempAge]
        mostOcurringAge = tempAge

print("Oldest: ",Oldest)
print("Youngest: ",Youngest)
print("MostOcurring: ",mostOcurringAge,"with",counter,"participations")


inputFile.close()