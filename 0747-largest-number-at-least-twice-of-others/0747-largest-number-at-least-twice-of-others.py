class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n=len(nums)
        largest=max(nums)
        index=nums.index(largest)
        small=float("-inf")
        for num in nums:
            if num!=largest:
                small=max(small,num)
        if largest>=2*small:
            return index
        else:
            return -1

            
            
    
        