def sortArrayByParity(nums):

    n=len(nums)
    start=0
    for i in  range(0,n):
        if nums[i] % 2 == 0:
            nums[start],nums[i]=nums[i],nums[start]
            start+=1
    return nums
nums=[3,5,8,9,4,9]
for i in sortArrayByParity(nums):
    print(i)