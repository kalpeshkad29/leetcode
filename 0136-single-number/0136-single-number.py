class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for k,v in freq.items():
            if v==1:
                return k

        