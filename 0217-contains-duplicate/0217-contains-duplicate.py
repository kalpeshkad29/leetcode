class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        seen={}
        for i in range(0,n):
            if nums[i] in seen:
                return True
            seen[nums[i]]=i
        return False

        