"""Class Books:

Data=[

{"id":100,"name":"python","price":350},

{"id":101,"name":"java","price":450),

{"id":102,"name":"Django","price":1300),

{"id":103,"name":"Html","price":1000},

{"id":104,"name":"Bootstrap","price":300}

]

Create methods for

a)list all Books
b)print details of specific book
c)update a Book
d)Delete a Book

"""


class Books:
    Data=[

{"id":100,"name":"python","price":350},

{"id":101,"name":"java","price":450},

{"id":102,"name":"Django","price":1300},

{"id":103,"name":"Html","price":1000},

{"id":104,"name":"Bootstrap","price":300}

]
    
    def list_all_books(self):
        print(Books.Data)

    def details_of_specific(self):
        self.n=int(input("Enter the id of the book: "))
        for i in Books.Data:
            if i.get("id")==self.n:
                print(i)

    def update(self,book_id,update_dict):
        # update_dict:dict
        self.update_dict=update_dict
        self.book_id=book_id
        for i in Books.Data:
            if i.get("id")==self.book_id:
                i.update(update_dict)
                print(Books.Data)

    def delete(self,book_id,to_delete):
        self.to_delete=to_delete
        self.book_id=book_id
        for i in Books.Data:
            if i.get("id")==self.book_id:
                del i [to_delete]
                print(i)

    def clear(self,book_id):
        self.book_id=book_id
        for i in Books.Data:
            if i.get("id")==self.book_id:
                i.clear()
                print(Books.Data)

        
                
                 


                    
                
obj=Books()   
# obj.list_all_books()  
# obj.details_of_specific()
# obj.update(100,{"name":"sai","price":450})
obj.delete(100,'price')
# obj.clear()