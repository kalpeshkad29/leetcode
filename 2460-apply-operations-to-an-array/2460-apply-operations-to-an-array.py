class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        result=[]
        for num in nums:
            if num!=0:
                result.append(num)
        while len(result)<n:
            result.append(0)
        return result

        