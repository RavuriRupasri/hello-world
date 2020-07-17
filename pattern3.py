num=int(input("Enter number of lines: "))
for i in range(1,num+1):
    print(" "*int(num-i),end='')
    print("*"*i)