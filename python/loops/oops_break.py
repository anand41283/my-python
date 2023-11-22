fruits=["kiwi","orange","apple","banana"]
for i in fruits:
    print(i)
    if(i=="apple"):
        break
print("after break")
for x in fruits:
    if(x=="apple"):
        break
    print(x)
   