class arethematic:
    num1:int
    num2:int
    def value_add(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("sum is ",self.num1+self.num2)
        

obj1=arethematic()
obj1.value_add(10,2)
obj1.add()    