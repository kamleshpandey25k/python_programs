def findlargestElement(num):
    largest=num[0]
    n=len(num)
    for i in range(0,n):
        # largest=max(largest,num[i])
        if largest < num[i]:
            largest=num[i]
    return largest
num=[10,60,20,70,30,90]
print(findlargestElement(num))