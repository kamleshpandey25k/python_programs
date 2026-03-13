file=open("docs.txt",'r')
#ans=file.read() # read all line are given number but return type is string
#ans=file.readline()# read one line return type string
ans=file.readlines() # read multiple line but return type is list wo won'n we paas number of character as argument
#readable () check file is readable or not
print(ans)
print(type(ans))
print(ans[0])
file.close()