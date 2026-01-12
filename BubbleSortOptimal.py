def bubbleSort(num):
    n=len(num)
    for i in range(n-1):
        isSorted=True
        for j in range(n-1-i):
            if num[j]>num[j+1]:
                isTrue=False
                num[j],num[j+1]=num[j+1],num[j]
        if isSorted:
            break
num=[10,20,30,40]
bubbleSort(num)
print(num)