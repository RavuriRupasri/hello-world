#Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.
x,y=list(map(int,input("Enter base and power: ").split()))
#print(pow(x,y))
print(x**y)