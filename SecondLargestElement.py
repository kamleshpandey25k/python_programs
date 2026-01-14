def secondLargestOptimal(num):
    first=float('-inf')
    s_largest=float('-inf')
    n=len(num)
    for i in range(0,n):
        if num[i] > first:
            s_largest=first
            first=num[i]
        elif s_largest < num[i] and num[i] != first :
             s_largest=num[i]
    return s_largest

def secondLargestElement(num):
    first=float('-inf')
    second=float('-inf')
    n=len(num)
    for i in range(0,n):
        first=max(first,num[i])

    for i in range(0,n):
        if second< num[i] and num[i]!=first:
          second = num[i]
    return second
num=[10,30,50,22,88,55,44]
print(secondLargestOptimal(num))