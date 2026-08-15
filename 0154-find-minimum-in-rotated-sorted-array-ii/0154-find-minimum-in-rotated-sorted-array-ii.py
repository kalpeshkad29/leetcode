class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        small=float("inf")
        for i in range(0,n):
            if nums[i]<small:
                small=nums[i]
        return small


        