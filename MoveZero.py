def moveZero(nums):
    idx=0
    n=len(nums)
    ans=[0]*n
  
    for i in range(n):
        if nums[i] !=0:
            ans[idx]=nums[i]
            idx+=1
    # while idx<n:
    #     ans[idx]=0
    #     idx+=1
    print(ans) 
nums=[2,0,5,4,0,3,1,0,7,8]
moveZero(nums)
  