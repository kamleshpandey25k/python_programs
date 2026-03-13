text="Hello Jay Shree Ram"
file="docs.txt"
myfile=open(file,'w')
myfile.write(text)
print(myfile)
# Access mode
# if file not present then w will create the file but in case of r if file not present then it will generate error
# r = open file read only
# r+ = open file read and write
# rb = open file read only binary formate
# rb+ = open file read and write binary formate
# w = open file for write only
# w+ = open file read and write 
# wb = open file write only binary formate
# wb+ = open file read and writein binary formate
# a = open file  for append
# a+ = open for append and read
# ab =open file for append in binary formate
# ab+ = open file for append and read in binary formate
