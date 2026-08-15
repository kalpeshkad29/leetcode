class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float("inf")
        n=len(nums)
        j=0
        total=0
        for i in range(n):
            total+=nums[i]

            while total>=target:
                mini=min(mini,i-j+1)
                total-=nums[j]
                j+=1
        if mini==float("inf"):
            return 0
        else:
            return mini
                   
                
        