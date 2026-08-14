class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        pos=[]
        neg=[]
        for num in nums:
            if num>0:
                pos.append(num)
            elif num<0:
                neg.append(num)
        return max(len(pos),len(neg))


        