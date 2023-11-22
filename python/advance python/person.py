class person:
    name:str
    age:int
    sex:str
    profession:str

    def add_person(self,name,age,sex,profession):
        self.name=name
        self.age=age
        self.sex=sex
        self.profession=profession

    def show(self):
        print("Name: "+self.name)
        print("age: ",self.age)
        print("sex: "+self.sex)
        print("profession: "+self.profession)
    def work(self):
        print(f"{self.name} is workig as {self.profession}")    
obj1=person()
obj1.add_person("anand",21,"male","developer") 
obj1.show()
obj1.work()    
print(dir(obj1))
