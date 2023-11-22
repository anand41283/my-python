#student.py

class student:
    rpllno:int
    name:str
    course:str
    def add_student(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def display(self):
        print("Roll no= ",self.rollno) 

obj1=student()
obj1.add_student(1,"anand","course")
obj1.display()







