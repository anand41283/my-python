class users:
    data=[
        {"id":1,"username":"anu","email":"anu@gmail.com","password":"password@123"},
        {"id":2,"username":"achu","email":"achu@gmail.com","password":"password@123"},
        {"id":3,"username":"ammu","email":"ammu@gmail.com","password":"password@123"},
        {"id":4,"username":"manu","email":"manu@gmail.com","password":"password@123"},
        {"id":5,"username":"Thanu","email":"thanu@gmail.com","password":"password@123"},
        {"id":6,"username":"ann","email":"ann@gmail.com","password":"password@123"},

    ]
    #get all data
    def get_all_data(self):
        return self.data
    def get_one(self):
        return self.data[0]
    def get_given_user(self,id):
        for i in self.data:
            if i.get("id")==id:
                return i
    def add_user(self,user1):
        self.data.append(user1)
    def delete(self,id2):
        for u in self.data:
            if u.get("id")==id2:
                self.data.remove(u)
                


            
    
obj=users()
# print(obj.get_all_data())   
# print(obj.get_one())
obj.delete(3)
print(obj.get_all_data())   




    