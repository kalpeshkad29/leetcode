class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        left=-1
        right=-1
        n=len(nums)
        max_num=nums[0]
        for i in range(n):
            max_num=max(nums[i],max_num)
            if nums[i]<max_num:
                right=i
        min_num=nums[-1]
        for i in range(n-1,-1,-1):
            min_num=min(nums[i],min_num)
            if nums[i]>min_num:
                left=i
        if right==-1:
            return 0
        return right-left+1
        