class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        for i in range(n):
            result[i]=nums[i]*nums[i]
        
        result2=sorted(result)
        return result2

        