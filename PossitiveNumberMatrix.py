def findpPossitiveNumber(nums):
     ans=[]
     for i in range(0,len(nums)):
          for j in range(0,len(nums[0])):
               if nums[i][j] >= 0:
                   ans.append(nums[i][j])
     return ans 
nums=[[-1,-2,-3],[4,5,6],[7,8,9]]
print(findpPossitiveNumber(nums))
