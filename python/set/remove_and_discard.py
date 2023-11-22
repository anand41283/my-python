s={1,2,3,4,5}
print(s)
s.remove(1)
print(s)
# s.remove(6)#show error
s.discard(2)
print(s)
s.discard(8)
print(s)#does not shows error
s.pop()
print(s)
s.clear()
print(s)
del s
print(s)