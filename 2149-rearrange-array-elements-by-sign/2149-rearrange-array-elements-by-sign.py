class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        result=[]
        for i in range(0,n):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
            
        for i in range(0,len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result
        