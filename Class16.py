# Animals - Part A, B

class Pet:
    def __init__(self,n,a,h,p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p

    #getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    #setters
    def setname(self,name):
        self.name = name
    def setAge(self,age):
        self.age = age
    def setHunger(self,hunger):
        self.hunger = hunger
    def setPlayful(self,playful):
        self.playful = playful
    def __str__(self):
        return (self.name + " is "+ str(self.age) + " years old")


# Pet1 = Pet("Rocko",4.5,False,True)

# print(Pet1.getName())
# print(Pet1.getAge())
# print(Pet1.getHunger())
# print(Pet1.getPlayful())

# Pet1.setname("Peluche")
# print(Pet1.getName())

class Dog(Pet):
    def __init__(self,Breed,FToy,name,age,hunger,playful):
        Pet.__init__(self,name,age,hunger,playful)
        self.Breed = Breed
        self.FavoriteToy = FToy

    def wantToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with "+ self.FavoriteToy)
        else: 
            return ("Dog doesn't wants to play")

class Cat(Pet):
    def __init__(self, name, age, hunger, playful,FP):
        Pet.__init__(self,name,age,hunger,playful)
        self.FavoritePlaceToSit = FP
    def wantToSit(self):
        if self.playful == False:
            print("The cat wants to sit in "+ self.FavoritePlaceToSit)
        else:
            print("The cat wants to play")
    def __str__(self):
        return (self.name + " likes to sit in " + self.FavoritePlaceToSit)

class Human:
    def __init__(self, name, pets):
        self.name = name
        self.pets = pets
    def hasPet(self):
        if len(self.pets) != 0:
            return "yes"
        else:
            return "no"
        

PitbullDog = Dog("Pitbull","Ball","Rocko",4.5,False,False) 
Play = PitbullDog.wantToPlay()
print([PitbullDog.Breed,PitbullDog.FavoriteToy,PitbullDog.name,PitbullDog.hunger,Play])

Cat1 = Cat("BolaDePelo",2,False,False,"BedsCat")
print(Cat1.name)
print(Cat1.age)
print(Cat1.hunger)
print(Cat1.playful)
print(Cat1.FavoritePlaceToSit)
Cat1.wantToSit()
print(Cat1)
print(PitbullDog)
Human1 = Human("alvarod",[PitbullDog])
print("-----------------")
# hasPet = Human1.hasPet()
print(Human1.hasPet())
print(Human1.pets[0].name)