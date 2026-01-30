d1={
    "name":"Ram",
    "age":30,
     "gender":"male",
     "state":"MP",
     "city" : "Rewa"

}
print(d1.values())
print(d1.keys())
print(d1.items())
for k in d1:
    print(k,d1[k])
for k in d1.items():
    ke,v=k #unpacking
    # ke=k[0]
    # v=k[1]
    print(ke,v)
print(sorted(d1))
print(min(d1))
print(max(d1))
#  print(sum(d1)) TypeError
d1.pop("name")
print(d1)
print(d1.popitem())