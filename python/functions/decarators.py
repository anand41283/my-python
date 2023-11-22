def smartdiv(func):
    def inner(a,b):
        print(" I am going to divide",a,"and",b)
        if b==0:
            print("#oops can not divide")
            return
        return inner
#def div(a,b):
# print(a/b)
# reslt=smartdiv(div)
# reslt(4,5)
@smartdiv #    