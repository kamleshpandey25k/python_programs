def printLowerTringle(nums):
    for i in range(0,len(nums)):
        for j in range(0,len(nums[0])):
            if i>=j:
                print(nums[i][j],end=" ")
        print("")
nums=[[1,2,3],[88,55,3],[6,4,2]]
printLowerTringle(nums)
