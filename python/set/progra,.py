names={'ann','kevin','paru'}

#remove ammu 
# names.remove("ammu")#here show error
names.discard("ammu")
print(names)
#remove "appu" without error
names.discard("ammu")
print(names)
#add kichu to the set
names.add("kichu")
print(names)
#add ["kevin","jeo","mithu"] to the set
s=["kevin","jeo","mithu"]
names.update(s)
print(names)
#length of the set name
print(len(names))
#clear out the elements
names.clear()
print(names)
#length
print(len(names))
#delt the full set
del names
print(names)