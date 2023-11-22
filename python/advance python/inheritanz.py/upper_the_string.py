class string:

    
    # def __init__(self,s):
    #     self.s=s
    def getstring(self):
        self.s=input("Enter the string to convert:")
        
    def printstring(self):
        return self.s.upper() 
    def test(self):
        self.getstring()
        print(f"After the conversion of the string is :{self.printstring()}")
        

obj=string()
obj.test()
        