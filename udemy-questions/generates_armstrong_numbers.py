#Generate Armstrong numbers
num=int(input("Enter the range to generate armstrong numbers\n"))
l=[]
for i in range(0,num+1):
    temp=i 
    sum1=0
    while(i>0):
            x=i%10
            sum1=sum1+x**3
            i=int(i/10)
    if(sum1==temp):
            l.append(temp)
    else:
            continue
print(l)