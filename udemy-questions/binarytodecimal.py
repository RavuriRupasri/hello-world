#binary to decimal
num=int(input("Enter the number: "))
base=1 
sum1=0
while(num!=0):
    x=num%10
    sum1=sum1+x*base
    num=int(num/10)
    base*=2
print(sum1)