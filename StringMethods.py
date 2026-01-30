s1="hello everyone how are you"
print(type(s1))
# 1 index()
print(s1.index("l"))
print(s1.index("one"))
# 2 count()
print(s1.count(" "))
print(s1.count("o"))
print(s1.count("-"))
# 3 startswith()
print(s1.startswith("He"))
print(s1.startswith("HH"))

#4 endswith()
print(s1.endswith("you"))
print(s1.endswith("hh"))

# 5 isdigit()
ss="123"
print(s1.isdigit())
print(ss.isdigit())

# 6 islower()
print(s1.islower())
print(s1.isupper())

# 7 upper()
print(s1.upper())

# 8 lower()
print(s1.lower())

# 9 replace(oidstr,newstr)
print(s1.replace("e","E"))
# 10 format()
print("sum of {} and {} is {}".format(10,20,10+20))

# 11 split() it returns list of str
l1=s1.split(" ")
print(l1)
for x in l1:
    print(x)
# 12 join(str)
str2=" ".join(l1)
print(str2)