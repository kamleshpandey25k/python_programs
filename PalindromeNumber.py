def isPalindrome(n):
 num=n;
 while num>0:
    lastDigit=num%10;
    result=(result*10)+lastDigit;
    num=num//10;
 if n==result:
    return True;
 else: 
    return False;

n=int(input("Enter the number"));
result=1
num=n

if isPalindrome:
    print(" It is palindrome");
else :
    print(" It is not palindrome");