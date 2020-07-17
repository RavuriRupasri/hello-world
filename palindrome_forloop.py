#This program prints true if the string is palindrome and false if it is not palindrome
string=input("Enter the string to check it is palindrome or not: ")
flag=0 
n=len(string)
for i in range(n//2+1):
    if(string[i]!=string[n-i-1]):
        flag=1 
        break
if(flag):
    print("It is not palindrome")
else:
    print("It is palindrome")