l1=[10,20,30,40,50]
print(type(l1))
l2=[10,20.50,True,'Ram',3+4,9+9j]
print(type(l2))
l3=[]
print(type(l3))
print(l3)
# how to access elements of the list : using index
print(l1[0],l1[1],l1[-4])

for x in l1:
    print(x,end=' , ')
print()
i=0
while i < len(l1) :
    print(l1[i], end=' ')
    i+=1
print()
# How to delete elements of the list

del l1[0]
print(l1)
# how to edit elements of the list
l1[0]=10
print(l1)
l1.append(99)
print(l1)
l1.insert(0,00)
print(l1)

l1.insert(10,40)
print(l1)