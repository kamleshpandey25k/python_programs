# how to create and initilize
d1={}
d2=dict()
d3={
    "name" : "Rahul",
    "age"  : 30,
    "state" :"MP",
     "city" :"Rewa"
}
print(d3)
print(d3["name"])
# how to access all keys and values
for k in d3:
    print(k,d3[k])
d3["name"]="Ram"
print(d3)
d3["pincode"]="4533234"
print(d3)
print(d3.keys())