n = int(input("Enter the range"))
a = 0
b = 1
x=2
print(a,b,end=' ')
while(x<n):
    c = a + b 
    a = b 
    b = c 
    print(b,end = ' ')
    x += 1
