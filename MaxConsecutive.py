def maxConsecutive(nums):
    count=1
    max_count=0
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            count+=1
        else:
            max_count=max(max_count,count)
            count=1
    return max(max_count,count)
nums=[0,0,1,1,0,1,2,2,2,2]
print(maxConsecutive(nums))
             