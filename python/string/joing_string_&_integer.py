quantity=3
item=567
price=45
print(f" i want {quantity} pieces of item {item} for {price}")
tust=" i want {} pieces of item {} for {}"
print(tust.format(quantity,item,price))

name="heric"
age=45
print(f"hello,{name} you are {age}")
tist="hello,{} you are {}"
print(tist.format(name,age))

bags=36
fruits="apple"
print(f"there are total of {bags} {fruits}")
test="there are total of {} {}"
print(test.format(bags,fruits))

name='SACHIN'
dept="better"
print(f"{name} is {dept}")
tsts="{} is {}"
print(tsts.format(name,dept))