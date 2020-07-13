a=[2,3,0,1,0,4,0,8]
i=0
for j in range(len(a)):
    if a[j]!=0:
        a[i],a[j]=a[j],a[i]
        i=i+1
print(a)