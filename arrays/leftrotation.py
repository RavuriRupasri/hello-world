n = int(input())
a = list(map(int,input().split()))[:n]
x = int(input("Enter no. of elements to be rotated left"))
for j in range(x):
    temp = a[0]
    for i in range(n - 1):
        a[i] = a[i+1]
    a[n-1] = temp
print(a)