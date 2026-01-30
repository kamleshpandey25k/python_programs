# In python str is a sequential data structure reprent with "", and '' it id index based data structure and it is hashable
s1="Hi friends my name ki kamlesh pandey"
print(s1)
print(hash(s1))
# How to create object , There are 6 way to create object of str

s1='Hello1'
s2="Hello2"
s3='''Hello 3'''
s4="""Hello 4"""
s5=str("Hello s5")
print(s1,s2,s3,s4,s5)
print(s5[-3])
for x in s5:
    print(x)
for i in range(0,len(s5)):
    print(s5[i])
ss=sorted(s1)
print(ss)
print(str(ss))