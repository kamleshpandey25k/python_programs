

def mergeArrays(num1,num2):
    num3=[]
    i=0
    j=0
    while i < len(num1) and j < len (num2):
        if num1[i] < num2[j]:
             if num1[i] not in num3:
               num3.append(num1[i])
             i+=1
        elif num1[i]> num2[j] :
            if num2[j] not in num3:
              num3.append(num2[j])
            j+=1
        else :
             if num1[i] not in num3:
                 num3.append(num1[i])
             i+=1
             j+=1
    while i < len(num1):
          if num1[i] not in num3:
             num3.append(num1[i])
          i+=1
    while j < len(num2):
          if num2[j] not in num3:
             num3.append(num2[j])
          j+=1
    print(num3)
ar1=[10,30,40,50]
ar2=[20,30,40,60]
mergeArrays(ar1,ar2)