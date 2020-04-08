#Class inheritance
class Team:
    def __init__(self,Name = "Name", NameOrigin = "Origin"):
        self.TeamName = Name
        self.TeamOrigin = NameOrigin

    def DefineTeamName(self,Name):
        self.TeamName = Name

    def DefineTeamOrigin(self,NameOrigin):
        self.TeamOrigin = NameOrigin


# #example de herencia
# class inheritanceClassName(ParentClass):
#     def __init__(self,input1,input2):
#         self.Atribute1 = input1
#         self.Atribute2 = input2
#         self.Atribute3 = 0
#     def Anothermethod (self):
#         Action(s)

class Player(Team):
    def __init__(self,PName,PPoint,TeamName,TeamOrigin):
        Team.__init__(self,TeamName,TeamOrigin)
        self.PlayerName = PName
        self.PlayerPoints = PPoint

    def setName(self,name):
        self.PlayerName = name
    
    def ScoredPoints(self):
        self.PlayerPoints += 1

    def __str__(self):
        return self.PlayerName + " has scored: " + str(self.PlayerPoints) + "points"

Player1 = Player("Sebastian",0,"Alianza Lima","Lima")


print(Player1.PlayerName)
Player1.ScoredPoints()
print(Player1.PlayerPoints)
print(Player1.TeamName)
print(Player1.TeamOrigin)
print(Player1)