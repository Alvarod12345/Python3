#introduction Class


# context
# class ClassName:
#     def __init__(self):
#         self.Attribute = 0
#     def AnotherFunction(self):
#        Action(s)


# Primera forma
class Team:
    def __init__(self):
        self.TeamName = "NaN"
        self.TeamOrigin = "NaN"

    def DefineTeamName(self,Name):
        self.TeamName = Name

    def DefineTeamOrigin(self,NameOrigin):
        self.TeamOrigin = NameOrigin

Team1 = Team()

print(Team1.TeamName) # Imprime la linea de codigo NaN
print("Name:")
Team1.DefineTeamName("Leons") # agerga "Leons" como Name
print(Team1.TeamName) # imprime Name

print(Team1.TeamOrigin) # Imprime la linea de codigo NaN
print("Origin:")
Team1.DefineTeamOrigin("NYC")# agerga "NYC" como Name
print(Team1.TeamOrigin) # imprime Name




# Segunda Forma
class Team2:
    def __init__(self,Name,Origin):
        self.TeamName = Name
        self.NameOrigin = Origin
Team2 = Team2("Alianza Lima","Lima")
print(Team2.TeamName)
print(Team2.NameOrigin)
        



# Tercera Forma
class Team3:
    def __init__(self,Name = "Universitario", Origin = "Lima"):
        self.TeamName = Name
        self.NameOrigin = Origin
Team3 = Team3()
print(Team3.TeamName)
print(Team3.NameOrigin)