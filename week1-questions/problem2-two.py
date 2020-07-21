a=[1,2,3,4,5]
n=len(a)
d=0
x=int(input("enter the no. of elements to be shifted"))
while(True):
    a[n-1],a[d]=a[d],a[n-1]
    d=d+1 
    n=n-1
    if(d==x):
        break
print(a)