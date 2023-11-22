


class vehicle:
    def __init__(self,name,max_speed,mileage): 
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def seating_capacity(self):
        print("The seating capacity",45)   
    
class bus(vehicle):
    def sai(self, name, max_speed, mileage,s_capacity=50):
        super().__init__(name, max_speed, mileage)
        self.s_capacity=s_capacity
    def display(self):    
        return f"The seating capacity of {self.name} is {self.s_capacity} passengers with {self.mileage} mileage at speed {self.max_speed}"

obj=bus('singam','6','5')      
# print(f"The seating capacity of {obj.name} is {obj.s_capacity} passengers with {obj.mileage} mileage at speed {obj.max_speed}")  
obj.sai('singam','60','5')
print(obj.display())
obj.seating_capacity()


        


        