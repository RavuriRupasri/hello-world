n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if(i == j or i > j):
            print(i+1,end = ' ')
        else:
            print(j+1,end = ' ')
    print()