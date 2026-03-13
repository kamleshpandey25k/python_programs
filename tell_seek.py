with open("abc.txt",'r') as file:
    #ans=file.readlines()
    print(file.tell())
    file.seek(10)
    rr=file.readlines()
    print(rr)
 