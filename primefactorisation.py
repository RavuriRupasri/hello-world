num=int(input())
while(num>1):
    for i in range(2,num+1):
        if(num%i==0):
            print(i,end=' ')
            break
    num=int(num/i)

