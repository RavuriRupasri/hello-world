#This program prints true if the string is palindrome and false if it is not palindrome
string=input("Enter the string to check if the string is palindrome or not: ")
print(string==string[::-1])
