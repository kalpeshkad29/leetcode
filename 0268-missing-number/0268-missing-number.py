class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        my_dict={}
        for i in range(n):
            if nums[i] in my_dict:
                my_dict[nums[i]]+=1
            else:
                my_dict[nums[i]]=1
        for i in range(n+1):
            if i not in my_dict:
                return i
                
        


            
        