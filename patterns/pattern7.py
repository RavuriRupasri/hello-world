num=int(input("Enter number of lines: "))
k=65
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(k),end=" ")
    k=k+1
    print( )