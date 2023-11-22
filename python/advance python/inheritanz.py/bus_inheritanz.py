class vehicle:
    name:str
    c:float
    seating_capacity:int
    bus_seat:int
    def __init__(self, name, seating_capacity=50):
        self.name=name
        self.seating_capacity=seating_capacity
        
    def fare(self):
        b=self.seating_capacity*100
        print("The fare charge for vehicle is ",b)
class Bus(vehicle):
    def fare(self):
        c=(self.seating_capacity*100)*0.1+self.seating_capacity*100
        print(f"The price after the 10% maintanance is {c} ") 
        # super().fare()
        
obj=Bus('bus')
print("Name of the vehicle :",obj.name)
print("Seating capacity of the vehicle ",obj.seating_capacity)
obj.fare() 


 
                    