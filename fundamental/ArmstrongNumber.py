

def isArmstrong(num):
     if num>= 0 and num <= 9 :
         return True;
     n=num;
     ans=0;
     while n>0:
          lastDigit=n%10;
          ans=ans+lastDigit**3;
          n=n//10;
     if num==ans:
       return True;
     else:
       return False;
  
nn=int(input("Enter the number"));
if isArmstrong(nn):
    print("It is Armstrong number");
else:
    print("It is not armstrong number");