a = [4,5,7,3,2]
for i in range(1,len(a),1):
    for j in range(i,0,-1):
        if(a[j-1]>a[j]):
            a[j],a[j-1] = a[j-1],a[j] 
print(a)