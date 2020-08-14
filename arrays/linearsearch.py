n = int(input())
a = list(map(int,input().split()))[:n]
temp = 0
search = int(input())
for i in range(n):
    if(a[i] == search):
        print("element is at the index: ",i)
        temp = 1
        break
if(temp == 0):
    print("The element is not found in the array.")
