# Mean, Median and Mode
mean=[3,5,4,7,8]
sum=0
c=0
for i in mean:
    sum+=i
    c+=1
print("Mean",sum/c)

l=[2,5,4,8,9]
c=0
i=0
sum=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]<l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
        j+=1
        
    i+=1
    c+=1
# print(l,c)
if c%2==0:
    median1=l[c//2]
    median2=l[c//2-1]
    median=(median1+median2)#3
else:
    median=l[c//2]#2
print("Median",median)


# mode
l= [1, 2, 3, 4, 2, 7, 8, 8, 3,9,9]  
lis=[]
for i in l:
    if i not in lis:
        lis.append(i)
print(lis)
            
