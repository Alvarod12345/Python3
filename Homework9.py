import random

class vehicle:
    def __init__(self,make,model,year,weight,nm = False,tsm = 0): #nm = NeedsMaintenance, ts = TripsSinceMaintenance
        self.Make = make
        self.Model = model
        self.Year = year    
        self.Weight = weight
        self.NM = nm
        self.TSM = tsm
        
    # getters
    def getMake(self):
        return self.Make
    def getModel(self):
        return self.Model 
    def getYear(self):
        return self.Year
    def getWeight(self):
        return self.Year
    def repair(self):
        self.TSM = 0
        self.NM = False
    
    # setters
    def setMake(self,make):
        self.Make = make
    def setModel(self,model):
        self.Model = model
    def setWeight(self,weight):
        self.Weight = weight


class cars(vehicle):
    def __init__(self,make,model,year,weight,isDriving = False):
        vehicle.__init__(self,make,model,year,weight)
        self.isDriving = isDriving 
    def drive(self):
        self.isDriving = True

    def stop(self):
        if self.isDriving:
            self.TSM += 1
            if self.TSM >=100:
                self.NM = True 
        self.isDriving = False

def random_class(car):
    drive_times = random.randint(1,105)
    for i in range(drive_times):
        car.drive()
        car.stop()

def print_car_specs(car):
    print("--------------CARS-------------------")
    print("make ",car.Make)
    print("model ", car.Model) 
    print("year ", car.Year)
    print("weight ", car.Weight)
    print("needs maintenace" , car.NM)
    print("trips since maintenance", car.TSM)

class plane(vehicle):
    def __init__(self, make, model, year, weight,flying = False):
        vehicle.__init__(self,make,model,year,weight)
        self.flying = flying
    def fly(self):
        if self.NM == True:
            return False
        self.flying = True
        return True

    def landing(self):
        if self.flying:
            self.TSM += 1
            if self.TSM >= 105:
                self.NM = True
        self.flying = False
        
def random_plane(plane,fly_times = None):
    fly_times = random.randint(1,105) if fly_times is None else fly_times
    for i in range(fly_times):
        is_flying = plane.fly()
        if is_flying:
            plane.landing()
        else:
            print("The plane can't fly until it's repaired.")
            plane.repair()
def print_plane_specs(plane):
    print("-----------PLANES----------------")
    print("make ", plane.Make)
    print("model ", plane.Model)
    print("year ", plane.Year)
    print("weight ", plane.Weight)
    print("needs maintenace ", plane.NM)
    print("trips since maintenance ", plane.TSM)

# cars data
car1 = cars("Ford","Mustang",1969,1800)
car2 = cars("Porsche","Carrera GT",2003,1380)
car3 = cars("Mazda","Rx7",1978,1310)

random_class(car1)
random_class(car2)
random_class(car3)

print_car_specs(car1)
print_car_specs(car2)
print_car_specs(car3)

#plane data
plane1 = plane("Boeing","747",1970,333400)
plane2 = plane("Boeing2","717",1970,333400)
plane3 = plane("Boeing3","714",1970,333400)

random_plane(plane1)
random_plane(plane2)
random_plane(plane3)

print_plane_specs(plane1)
print_plane_specs(plane2)
print_plane_specs(plane3)
