arr=[2,3,0,1,0,4,0,8]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if(arr[j]!=0):
            continue
        else:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)