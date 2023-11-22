n1=10
n2=20
n3=30

# print((n1<n2) and (n2>n3))
#10<20   and    20>30
# true           false
# out=false
# print((n1<n2) and (n2<n3))
#10<20   and    20<30
# true           true
# out=true
# print((n1>n2) and (n2<n3))
#10>20   and    20<30
# false          true
# out=false
# print((n1>n2) and (n2>n3))
#10>20   and    20>30
# false           false
# out=false


#OR Operator

# print((n1<n2) or (n2>n3))
#10<20   or    20>30
# true           false
# out=true
# print((n1<n2) or (n2<n3))
#10<20   or    20<30
# true           true
# out=true
# print((n1>n2) or (n2<n3))
#10>20   or    20<30
# false          true
# out=true
# print((n1>n2) or (n2>n3))
#10>20   or    20>30
# false           false
# out=false

#not operator
# print(not((n1<n2) and (n2<n3)))
# not(10<20 and 20<30)
# not(true and true )
# false
print(not((n1>n2) or (n2<n3)))