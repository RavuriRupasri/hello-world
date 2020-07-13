a=[1,2,3,4,5]
for i in range(2):
    x=a[len(a)-1]
    for j in range(len(a)-1,0,-1):
        a[j]=a[j-1]
    a[0]=x
print(a)