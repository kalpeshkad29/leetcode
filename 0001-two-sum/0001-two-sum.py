class Solution:
    def twoSum(self, nums, target):
        n=len(nums)
        seen={}
        for i in range(n):
            need=target-nums[i]
            if need in seen:
                return [seen[need],i]
            seen[nums[i]]=i



            

        

        

        

    