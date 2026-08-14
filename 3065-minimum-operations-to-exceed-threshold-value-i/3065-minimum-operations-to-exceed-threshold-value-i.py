class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        for i in range(0,n):
            if nums[i]<k:
                count+=1
        return count
        