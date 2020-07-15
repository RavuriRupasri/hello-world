#Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.

def fact(num):
    if(num==0):
        return 1 
    else:
        return num*fact(num-1)
num=int(input("Enter the number to find the factorial: "))
while(num<0):
    num=int(input("Factorial cannot be executed for a negative number\nEnter a number greater than or equal to 0\n"))
print("The factorial of a given number is: ",fact(num))