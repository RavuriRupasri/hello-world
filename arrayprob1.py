arr = [2, 3, 0, 1, 0, 4, 0, 8]
ar1=[]
x=arr.count(0)
for i in range(len(arr)):
    if arr[i]!=0:
        ar1.append(arr[i])
for i in range(x):
    ar1.append(0)
print(ar1)