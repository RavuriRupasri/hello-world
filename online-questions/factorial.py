#Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.
num=int(input("Enter the number to find the factorial: "))
fact=1 
while(num<0):
    num=int(input("Factorial cannot be executed for a negative number\nEnter a number greater than or equal to 0\n"))
for i in range(1,num+1):
    fact=fact*i
print("The factorial of a given number is: ",fact)