def upToPrime(n):
    prime_number=[]
    for i in range (2,n+1):
        count=0
        for j in range(2,i):
            if i % j==0:
                count+=1
                break
        if count==0:   
          prime_number.append(i)
    print(prime_number)
upToPrime(50)
             
