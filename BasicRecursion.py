count = 0
def printName():
    global count
    if count == 5:
        return
    print("Ram")
    count = count + 1
    printName()
printName()
