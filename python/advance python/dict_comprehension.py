# s=[1,2,3,4,5,6,7]
# b=['A','B','C','D','E','F','G']
# dicti={t:v for (t,v)in zip(s,b) }
# # print(dicti)
# for i in b:
#     dic=dict.fromkeys(range(1,8),i)
# print(dic)


#dictionary comprehension 
"""
We can create dictionaries using simple expressions. A dictionary comprehension takes the form

"""
words=['data','science','machine','learning']
print([len(i) for i in words])


print({i:len(i) for i in words})


print({x:y})