def hcf(n1,n2):
    min_value=min(n1,n2)
    ans=0
    for i in range(min_value,0,-1):
        if n1 % i ==0 and n2 % i ==0 :
           ans=i
           break
    print(ans)
hcf(10,20)
