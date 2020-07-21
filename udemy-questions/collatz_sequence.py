#Collatz Sequence
num=int(input("Enter the number: "))
count=0
while(num!=1):
    print(num,end=' ')
    if(num%2==0):
        num=int(num/2)
        count=count+1 
    else:
        num=int(3*num+1)
        count=count+1 
print(num,end=' ')
print("\nIt took {} steps.".format(count))
