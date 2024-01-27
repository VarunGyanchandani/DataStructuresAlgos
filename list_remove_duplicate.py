a=[1,1,1,2,2,3,4,4,5,5,5]
b=[]
for e in a:
    if e not in b:
        b.append(e)

print(a)
print(b)