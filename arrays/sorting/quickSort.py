def partition(a,low,high):
    i = low
    pivot = a[high]
    for j in range(low,high):
        if(a[j]<pivot):
            a[i],a[j] = a[j],a[i]
            i = i+1
    a[i],a[high]  = a[high],a[i]
    return (i)

def quickSort(a,low,high):
    if(low<high):
        p = partition(a,low,high)
        quickSort(a,low,p-1)
        quickSort(a,p+1,high)

n = int(input())
a = list(map(int,input().split()))[:n]
quickSort(a,0,n - 1)
print("Sorted Array is: ",a)