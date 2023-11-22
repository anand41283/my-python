def name():
    return "anand"
def arith_operators(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    h=a%b
    i=a**b
    j=a//b
    return f"sum={c},difference={d}\nproduct={e},division={f}\nreminder={h},power={i} floor division={j}"    
    
def count(s):
    count_v=0
    count_c=0
    for i in s:
        if i in "aeiouAEIOU":
            count_v+=1
        else:
            count_c+=1
    return f"count of vowels = {count_v}\ncount of consonants = {count_c}"   

def ten_numbers():
    for i in range(1,11):
        print(i)   

def spcl_char(s):
    li=[]
    for i in s:
        if i not in "abcdefghijklmnopqrstuvwxuzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            li.append(i)
    return li

    


  

  

   

