class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        seen={}
        for i in range(0,n):
            if nums[i] in seen:
                if abs(i-seen[nums[i]]) <=k:
                    return True
            seen[nums[i]]=i
        return False
        