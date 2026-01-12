def fibon(num):
    if num ==0 or num==1:
        return num
    return fibon(num-1)+fibon(num-2)
def fibon2(num):
    a,b=0,1
    for _ in range(num):
        print(a, end=" ")
        a,b=b,a+b
    return a
print(fibon2(9))