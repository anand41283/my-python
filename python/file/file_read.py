# #open(<file_name with location>,<access_mode(read or write)>)
# p=open("C:\\Users\\USER\\Desktop\\python\\file\\ss.txt","r")
# c=p.read()
# print(c)
# p.close()


# open(<file_name with location>,<access_mode(read or write)>)
# p=open("C:\\Users\\USER\\Desktop\\python\\file\\ss.txt","r")
# c=p.read(10)
# b=p.read(8)
# print(c)
# print(b)
# p.close()#don't clear


#aslist

# p=open("C:\\Users\\USER\\Desktop\\python\\file\\ss.txt","r")
# c=p.readlines()
# print(c)
# p.close()


#read by loop
#open(<file_name with location>,<access_mode(read or write)>)
# p=open("C:\\Users\\USER\\Desktop\\python\\file\\ss.txt","r")
# for i in p:
#     print(i)
# p.close()  

# writ method
# p=open("C:\\Users\\USER\\Desktop\\python\\file\\cc.txt","w")
# p.write("bmw\nbenz\n")
# p.writelines(['apple\n','mango\n','kiwi'])
# p.close

# #writing to existing txt (it will remove all content from the existing txt and then write )
# p=open("C:\\Users\\USER\\Desktop\\python\\file\\bb.txt","w")
# p.write("bmw\nbenz\n")

# #append
# p=open("C:\\Users\\USER\\Desktop\\python\\file\\cc.txt","a")
# p.write("\nmustank\nhummer\n")
# #it will also clreate new file when we type non file name
# #it is also same as the write

#remove a file
import os 
# os.remove("C:\\Users\\USER\\Desktop\\python\\file\\cc.txt")

if os.path.exists("C:\\Users\\USER\\Desktop\\python\\file\\cc.txt"):
    print("present")
else:
    print("not present")
    

#removing (blank folder)   

os.rmdir("C:\\Users\\USER\\Desktop\\python\\file\\jackei") 

       

       