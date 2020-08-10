#a = [4,5,7,3,2]
n = int(input())
a = list(map(int,input().strip().split()))[:n]
for i in range(n):
    mini = i
    for j in range(i+1,n):
        if(a[mini] > a[j]):
            mini = j 
    a[mini],a[i] = a[i],a[mini]
print(a)
