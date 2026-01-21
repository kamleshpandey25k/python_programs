def maxSubArray(nums):
    cur_sum=0
    max_sum=nums[0]
    for i in range(len(nums)):
        cur_sum+=nums[i]
        if max_sum <cur_sum:
            max_sum=cur_sum
        if cur_sum<0:
            cur_sum=0
    return max_sum
nums=[-1,-2,3,4,8]
print(maxSubArray(nums))