"""2. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.            
(Just try )
"""
class generator:
    def __init__(self,range):
        self.range=range
    def div_by7(self):
        li=[]
        for i in range(1,self.range+1):
            if i%7==0:
                li.append(i)
        print(li)          
obj=generator(20) 
obj.div_by7()                 