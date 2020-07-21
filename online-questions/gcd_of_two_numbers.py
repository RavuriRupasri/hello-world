#GCD of two numbers
x,y=list(map(int,input("Enter two numbers: ").split()))
a=min(x,y)
b=max(x,y) 
while(a>0):
    c=int(b%a)
    b=a 
    a=c 
print("The GCD of {} and {} is {}".format(x,y,b))