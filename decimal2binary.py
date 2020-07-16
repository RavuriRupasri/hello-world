#decimal to binary
#print(bin(123))
num=int(input("Enter the number: "))
l=[]
while(num>0):
    x=num%2 
    l.append(x)
    num=int(num/2) 
print('ob',end='')
for i in range(len(l)-1,-1,-1):
    print(l[i],end='')