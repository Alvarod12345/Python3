#File I/O

# File = open("Filename","r")
# File.close()

VacationSpots = ["London","Paris","NYC","Iceland"]
VacationFile = open("VacationPlaces","w")
for Spots in VacationSpots:
    VacationFile.write(Spots + "\n")
VacationFile.close()
VacationFile = open("VacationPlaces","r")
first = VacationFile.readline()
print(first)
second = VacationFile.readline()
print(second)
thrid = VacationFile.readline()
print(thrid)
fourth = VacationFile.readline()
print(fourth)
for line in VacationFile:
    print(line,end= "")


# for line in VacationFile:
#     print(line)
# TheWholeFile = VacationFile.read()

# print(TheWholeFile)
# # print(Spots)
# print("done")
VacationFile.close() #close

FinalSpot = "Thai"
VacationFile = open("VacationPlaces","a")
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces","r")
for line in VacationFile:
    print(line,end= "\n\n")

VacationFile.close()

# for i in range(5):
#     with open("VacationPlaces"+str(i),"r") as VacationFile:
#         for line in VacationFile:
#             print(line)
# VacationFile.read()

# VacationFile.close()

