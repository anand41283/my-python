class employee:
    employee_data=[
        {"emp_id":1000,"emp_name":"anand","dept":"developer","salary":1300000},
        {"emp_id":1001,"emp_name":"sai","dept":"sweeper","salary":8000},
        {"emp_id":1002,"emp_name":"abhira,","dept":"attender","salary":13000},
        {"emp_id":1004,"emp_name":"danish","dept":" mern developer","salary":130000},
        {"emp_id":1005,"emp_name":"nisha,","dept":"driver","salary":20000}
    ]
    def print_all(self):
        return self.employee_data
    def get_given_employee(self,id):
        for i in self.employee_data:
            if i.get("emp_id")==id:
                return i
    def add_employee(self,user1):
        self.employee_data.append(user1) 
    def update(self,id,user2):
        for i in self.employee_data
           

obj=employee()
# print(obj.print_all())  
print(obj.get_given_employee(1000)) 
user1={"emp_id":1000,"emp_name":"suiiii","dept":"developer","salary":1300000} 
obj.add_employee(user1)
# print(obj.print_all())
user2={"emp_id":1000,"emp_name":"sikku","dept":"developer","salary":1300000}
obj.update(1000,user2)
print(obj.print_all())

               