def countingSort(a,maxx):
    indexArray = [0]*(maxx+1)
    for i in range(len(a)):
        indexArray[a[i]] = indexArray[a[i]] + 1 
    indexArray[0] = indexArray[0] - 1
    for i in range(1,maxx+1):
        indexArray[i] = indexArray[i] + indexArray[i-1]
    result = [None]*len(a)
    for element in a:
        result[indexArray[element]] = element
        indexArray[element] = indexArray[element] - 1
    return result

n = int(input())
a = list(map(int,input().split()))[:n]
maxx = max(a)
result = countingSort(a,maxx)
print(result)