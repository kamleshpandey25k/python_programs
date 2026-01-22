def shellStock(nums):
    # min_value=min(nums)
    # max_value=max(nums)
    min_value=float("inf")
    max_value=float("-inf")
    for i in nums:
        if i > max_value:
            max_value=i
        if i <min_value :
            min_value=i
           
    profit=max_value-min_value
    return profit
nums=[1,5,2,3,8,6]
print(shellStock(nums))