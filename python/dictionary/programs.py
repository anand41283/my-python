# create a empty dictionary

dict={}
print(dict)

# create a dictionary course with key: course_name,pass_out,college

course={'course_name': 'Bsc omputer science','passout':'2020 to 2023','college':'AVAH arts ad science college'}
print(course)

#change the value of pass_out year 2018 to 2019

course['passout']='2018 to 2019'
print(course)

#add new item location to th dict course using update

course.update({'location':'kozhikode'})
print(course)

# print each key in dict course

for i in course:
    print(i)

# print each values in the dict course    
for i in course.values():
    print(i)

# print each items in the dict course    

for i in course.items():
    print(i)
#remove the item college

course.pop('location')    
print(course)

# find the length of dictionary
print(len(course))

#  clear out the dictionary
course.clear()
print(course)

# delete the dictionary completly
del course
print(course)
