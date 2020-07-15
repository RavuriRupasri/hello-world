num=int(input("Enter the number greater than zero\n"))
while(1):
    if(num==4 or num== 16 or num== 37 or num== 58 or num==20 or num== 42 or num== 89 or num==145):
        print("It is not a happy number\n")
        break
    sum1=0
    while(num>0):
        x=num%10
        sum1=sum1+x*x
        num=num/10
    if(sum1==1):
        print("It is a happy number\n")
        break
    if(sum1==0):
        print("Code canot be executed\n")
        break
    num=sum1