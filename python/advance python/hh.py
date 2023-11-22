def smartdiv(div):
    def inner (a,b):
        print("im going divide",a,"and",b)
        if b==0:
            print("can not divide")
        else:
            div(a,b)
               
    return inner        
            
# def div(a,b):
#     print(a/b)
#     res=smartdiv(div)
#     res(4,5)

    
# """using decorator"""
@smartdiv
def div(a,b):
    print(a/b)
div(4,5)
div(4,0)


# def plus_one(number):
#     def add_one(number):
#         return number+1
#     result=add_one(number)
#     return result
# print(plus_one(4))



# li=[1,2,3,4,5]
# l1=[6,7,8,9]
# c=li.add(l1)
# print(c)

