#Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
num=int(input("Enter the number greater than zero\n"))
while(1):
    if(num==4 or num== 16 or num== 37 or num== 58 or num==20 or num== 42 or num== 89 or num==145):
        print("It is not a happy number\n")
        break
    sum1=0
    while(num>0):
        x=num%10
        sum1=sum1+x*x
        num=int(num/10)
    if(sum1==1):
        print("It is a happy number\n")
        break
    if(sum1==0):
        print("Code cannot be executed\n")
        break
    num=sum1