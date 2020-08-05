n = int(input())
a = list(map(int,input().split()))[:n]
x = int(input("Enter no. of elements to be rotated right: "))
for j in range(x):
    temp = a[len(a) - 1]
    for i in range(len(a)-1,0,-1):
        a[i] = a[i-1]
    a[0] = temp
print(a)