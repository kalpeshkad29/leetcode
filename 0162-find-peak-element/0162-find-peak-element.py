class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        high=float("-inf")
        high_idx=0

        for i in range(0,n):
            if nums[i]>high:
                high=nums[i]
                high_idx=i
        return high_idx
    

        