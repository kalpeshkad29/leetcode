class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq={}
        for i in range(n-k+1):
            s=set(nums[i:i+k])
            for num in s:
                freq[num]=freq.get(num,0)+1
        ans=-1
        for k,v in freq.items():
            if v==1:
                ans=max(ans,k)
        return ans

        
        