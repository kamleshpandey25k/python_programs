def sumOFElements(nums):
    sum=0
    for i in range (0,len(nums)):
        for j in range(0,len(nums[0])):
            sum+=nums[i][j]
    return sum
nums=[[1,2,3],[4,5,6],[7,8,9]]
print(sumOFElements(nums))
