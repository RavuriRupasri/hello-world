n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if(j <= i):
            print(i+1,end = ' ')
        else:
            print(j+1,end = ' ')
    print()