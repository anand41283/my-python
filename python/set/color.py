color={"green","red","white"}


#write the program to add "blue" to the set color

color.add("blue")
print(color)
#find length of the set
print(len(color))
#add 'black','yellow','pink'
color2={'black','yellow','pink'}
color.update(color2)
print(color)
s=set()#create empty set
print(type(s))
s1={3,4,5,6,7,4,5,10}#update
s2={1,2,21,3,1,True}
s2.update(s1)
print(s2)