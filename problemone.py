arr=[2,3,0,1,0,4,0,8]
x=arr.count(0)
for i in range(x):
    arr.remove(0)
    arr.append(0)
print(arr)