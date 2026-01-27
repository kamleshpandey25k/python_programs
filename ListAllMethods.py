# list methods
# 1 append()
lis=[10,20,30,40,50,60,70]
print(lis)
lis.append(90)
print(lis)
#2 insert()  it add the value specific possition
lis.insert(0,100)
print(lis)
#3 remove() it remove the elements based on value not index
lis.remove(100)
print(lis)
# 4 pop() it is used to delete specific index possition value if dont mention index then last value will be deleted
lis.pop()
print(lis)
lis.pop(0)
print(lis)
# 5 clear() it is used to delete all data of the list
#lis.clear()
print(lis)
# 6 copy() method  is it used to copy the elements from one list to another list
#lis2=lis.copy()
lis2=list(lis)
print(lis2)
lis.append(200)
print(lis2)
# 7 list() it is used to copy list
# 8 count(value) it returns total number of value which we provided inside parameter 
print(lis.count(20))
# 9 extend() it is used to add the list at the last possition
lis.extend(lis2)
print(lis)
# 10 reverse() reverse of the list
lis.reverse()
print(lis)
# 11 sort() sort the list 
lis.sort()
print(lis)