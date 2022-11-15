a=[2,4,5,8,9,9,8,3]
l=[]
for i in a:
    if i not in l:
        l.append(i)
print(l)